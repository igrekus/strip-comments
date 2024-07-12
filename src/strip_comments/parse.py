import re
from typing import Tuple

import strip_comments.languages as languages
from strip_comments.models import Block, Node, Options, Token
from strip_comments.stack import Stack

__all__ = [
  'parse'
]


def _consume(value: str, remaining: str) -> Tuple[str, str]:
    return value, remaining[len(value):]


def _scan(remaining: str, regex: re.Pattern, type_='text'):
    match_ = regex.match(remaining)
    if match_:
        _, tail = _consume(match_[0], remaining)
        return tail, Token(type_, match_[0], match_)
    return remaining, None


def parse(input_: str, options: Options) -> Block:

    if not isinstance(input_, str):
        raise ValueError('Expected input to be a string')

    cst = Block(type_='root', nodes=[])
    stack = Stack([cst])
    name = options.language.lower()
    lang = getattr(languages, name, None)

    if lang is None:
        raise ValueError(f'Language {name} is not supported by strip-comments')

    LINE_REGEX = lang.get('LINE_REGEX', None)
    BLOCK_OPEN_REGEX = lang.get('BLOCK_OPEN_REGEX', None)
    BLOCK_CLOSE_REGEX = lang.get('BLOCK_CLOSE_REGEX', None)

    block = cst
    remaining = input_
    prev: Node | None = None

    source = list(filter(bool, [BLOCK_OPEN_REGEX, BLOCK_CLOSE_REGEX]))
    triple_quotes = False

    if all(el.pattern == r'^"""' for el in source):
        triple_quotes = True

    while remaining != '':
        # escaped characters
        remaining, token = _scan(remaining, languages.ESCAPED_CHAR_REGEX, 'text')
        if token:
            prev, block = stack.push(Node.from_token(token), prev, block)
            continue

        # quoted strings
        if block.type != 'block' and (not prev or not re.compile(r'\w$').search(prev.value)) and not (triple_quotes and remaining.startswith('"""')):
            remaining, token = _scan(remaining, languages.QUOTED_STRING_REGEX, 'text')
            if token:
                prev, block = stack.push(Node.from_token(token), prev, block)
                continue

        # newlines
        remaining, token = _scan(remaining, languages.NEWLINE_REGEX, 'newline')
        if token:
            prev, block = stack.push(Node.from_token(token), prev, block)
            continue

        # block comment open
        if BLOCK_OPEN_REGEX and options.block and not (triple_quotes and block.type == 'block'):
            remaining, token = _scan(remaining, BLOCK_OPEN_REGEX, 'open')
            if token:
                prev, block = stack.push(Block(type_='block'), prev, block)
                prev, block = stack.push(Node.from_token(token), prev, block)
                continue

        # block comment close
        if BLOCK_CLOSE_REGEX and block.type == 'block' and options.block:
            remaining, token = _scan(remaining, BLOCK_CLOSE_REGEX, 'close')
            if token:
                try:
                    newline = token.match.groups()[0]
                except LookupError:
                    newline = ''
                prev, block = stack.push(Node.from_token(token, newline), prev, block)
                block = stack.pop(block)
                continue

        # line comment
        if LINE_REGEX and block.type != 'block' and options.line:
            remaining, token = _scan(remaining, LINE_REGEX, 'line')
            if token:
                prev, block = stack.push(Node.from_token(token), prev, block)
                continue

        # Plain text (skip 'C' since some languages use 'C' to start comments)
        remaining, token = _scan(remaining, re.compile(r'^[a-zABD-Z0-9\t ]+'), 'text')
        if token:
            prev, block = stack.push(Node.from_token(token), prev, block)
            continue

        value, remaining = _consume(remaining[0], remaining)
        prev, block = stack.push(Node(type_='text', value=value), prev, block)

    return cst
