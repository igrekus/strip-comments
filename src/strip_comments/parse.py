import re
from typing import Tuple

import strip_comments.languages as languages
from strip_comments.models import Block, Node, Token

__all__ = [
  'parse'
]


ESCAPED_CHAR_REGEX = re.compile(r'^\\.')
QUOTED_STRING_REGEX = re.compile(r'^([\'"`])((?:\\\1|[^\1])+?)(\1)')
NEWLINE_REGEX = re.compile(r'^\r*\n')


def _consume(value: str, remaining: str) -> Tuple[str, str]:
    return value, remaining[len(value):]


def _scan(remaining: str, regex: re.Pattern, type_='text'):
    match_ = regex.match(remaining)
    if match_:
        _, tail = _consume(match_[0], remaining)
        return tail, Token(type_, match_[0], match_)
    return remaining, None


def _pop(stack, block):
    if block.type == 'root':
        raise SyntaxError('Unclosed block comment')

    stack.pop()
    return stack[len(stack) - 1]


def _push(stack, node, prev, block):
    # mutates
    if prev and prev.type == 'text' and node.type == 'text':
        prev.value += node.value
        return prev, block

    block.push(node)
    if hasattr(node, 'nodes'):
        stack.append(node)
        block = node
    prev = node
    return prev, block


def parse(input_, **kwargs):

    if not isinstance(input_, str):
        raise ValueError('Expected input to be a string')

    cst = Block(type_='root', nodes=[])
    stack = [cst]
    name = kwargs.get('language', 'javascript').lower()
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
        remaining, token = _scan(remaining, ESCAPED_CHAR_REGEX, 'text')
        if token:
            prev, block = _push(stack, Node.from_token(token), prev, block)
            continue

        # quoted strings
        if block.type != 'block' and (not prev or not re.compile(r'\w$').search(prev.value)) and not (triple_quotes and remaining.startswith('"""')):
            remaining, token = _scan(remaining, QUOTED_STRING_REGEX, 'text')
            if token:
                prev, block = _push(stack, Node.from_token(token), prev, block)
                continue

        # newlines
        remaining, token = _scan(remaining, NEWLINE_REGEX, 'newline')
        if token:
            prev, block = _push(stack, Node.from_token(token), prev, block)
            continue

        # block comment open
        if BLOCK_OPEN_REGEX and kwargs.get('block', None) and not (triple_quotes and block.type == 'block'):
            remaining, token = _scan(remaining, BLOCK_OPEN_REGEX, 'open')
            if token:
                prev, block = _push(stack, Block(type_='block'), prev, block)
                prev, block = _push(stack, Node.from_token(token), prev, block)
                continue

        # block comment close
        if BLOCK_CLOSE_REGEX and block.type == 'block' and kwargs.get('block', None):
            remaining, token = _scan(remaining, BLOCK_CLOSE_REGEX, 'close')
            if token:
                try:
                    newline = token.match.groups()[0]
                except LookupError:
                    newline = ''
                prev, block = _push(stack, Node.from_token(token, newline), prev, block)
                block = _pop(stack, block)
                continue

        # line comment
        if LINE_REGEX and block.type != 'block' and kwargs.get('line', None):
            remaining, token = _scan(remaining, LINE_REGEX, 'line')
            if token:
                prev, block = _push(stack, Node.from_token(token), prev, block)
                continue

        # Plain text (skip 'C' since some languages use 'C' to start comments)
        remaining, token = _scan(remaining, re.compile(r'^[a-zABD-Z0-9\t ]+'), 'text')
        if token:
            prev, block = _push(stack, Node.from_token(token), prev, block)
            continue

        value, remaining = _consume(remaining[0], remaining)
        prev, block = _push(stack, Node(type_='text', value=value), prev, block)

    return cst
