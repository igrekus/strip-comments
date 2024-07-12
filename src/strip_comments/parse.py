import re
from typing import Tuple

import strip_comments.languages as languages
from strip_comments.models import Block, Node, Options, Token
from strip_comments.stack import Stack

__all__ = [
  'parse'
]


def parse(source: str, options: Options) -> Block:

    stack = Stack()

    lang = options.language
    line_regex: re.Pattern | None = lang.get('LINE_REGEX', None)
    block_open_regex: re.Pattern | None = lang.get('BLOCK_OPEN_REGEX', None)
    block_close_regex: re.Pattern | None = lang.get('BLOCK_CLOSE_REGEX', None)

    remaining = source

    triple_quotes = False
    if all(el.pattern == r'^"""' for el in filter(bool, [block_open_regex, block_close_regex])):
        triple_quotes = True

    while remaining != '':

        # escaped characters
        remaining, token = _scan(remaining, languages.ESCAPED_CHAR_REGEX, 'text')
        if token:
            stack.push(Node.from_token(token))
            continue

        # quoted strings
        if not stack.is_block and (not stack.is_prev_exists or not re.compile(r'\w$').search(stack.prev_value)) and not (triple_quotes and remaining.startswith('"""')):
            remaining, token = _scan(remaining, languages.QUOTED_STRING_REGEX, 'text')
            if token:
                stack.push(Node.from_token(token))
                continue

        # newlines
        remaining, token = _scan(remaining, languages.NEWLINE_REGEX, 'newline')
        if token:
            stack.push(Node.from_token(token))
            continue

        # block comment open
        if block_open_regex and options.block and not (triple_quotes and stack.is_block):
            remaining, token = _scan(remaining, block_open_regex, 'open')
            if token:
                stack.push(Block(type_='block'))
                stack.push(Node.from_token(token))
                continue

        # block comment close
        if block_close_regex and stack.is_block and options.block:
            remaining, token = _scan(remaining, block_close_regex, 'close')
            if token:
                try:
                    newline = token.match.groups()[0]
                except LookupError:
                    newline = ''
                stack.push(Node.from_token(token, newline))
                stack.pop()
                continue

        # line comment
        if line_regex and not stack.is_block and options.line:
            remaining, token = _scan(remaining, line_regex, 'line')
            if token:
                stack.push(Node.from_token(token))
                continue

        # Plain text (skip 'C' since some languages use 'C' to start comments)
        remaining, token = _scan(remaining, re.compile(r'^[a-zABD-Z0-9\t ]+'), 'text')
        if token:
            stack.push(Node.from_token(token))
            continue

        value, remaining = _consume(remaining[0], remaining)
        stack.push(Node(type_='text', value=value))

    return stack.cst


def _consume(value: str, remaining: str) -> Tuple[str, str]:
    return value, remaining[len(value):]


def _scan(source: str, regex: re.Pattern, type_='text'):
    if match := regex.match(source):
        _, tail = _consume(match[0], source)
        return tail, Token(type_, match[0], match)
    return source, None
