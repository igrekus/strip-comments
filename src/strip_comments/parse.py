import re

import strip_comments.languages as languages
from strip_comments.models import Block, Node, Token

__all__ = [
  'parse'
]


ESCAPED_CHAR_REGEX = re.compile(r'^\\.')
QUOTED_STRING_REGEX = re.compile(r'^([\'"`])((?:\\\1|[^\1])+?)(\1)')
NEWLINE_REGEX = re.compile(r'^\r*\n')


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
    token = ''
    prev: Node | None = None

    source = list(filter(bool, [BLOCK_OPEN_REGEX, BLOCK_CLOSE_REGEX]))
    triple_quotes = False

    if all(el.pattern == r'^"""' for el in source):
        triple_quotes = True

    def consume(value):
        nonlocal remaining
        remaining = remaining[len(value):]
        return value

    def scan(regex: re.Pattern, type_='text'):
        match_ = regex.match(remaining)
        if match_:
            consume(match_[0])
            return Token(type_, match_[0], match_)

    def push(node):
        nonlocal prev
        nonlocal block
        nonlocal stack

        if prev and prev.type == 'text' and node.type == 'text':
            prev.value += node.value
            return

        block.push(node)
        if hasattr(node, 'nodes'):
            stack.append(node)
            block = node
        prev = node

    def pop():
        nonlocal stack
        nonlocal block

        if block.type == 'root':
            raise SyntaxError('Unclosed block comment')

        stack.pop()
        block = stack[len(stack) - 1]

    while remaining != '':
        # escaped characters
        if token := scan(ESCAPED_CHAR_REGEX, 'text'):
            push(Node.from_token(token))
            continue

        # quoted strings
        if block.type != 'block' and (not prev or not re.compile(r'\w$').search(prev.value)) and not (triple_quotes and remaining.startswith('"""')):
            if token := scan(QUOTED_STRING_REGEX, 'text'):
                push(Node.from_token(token))
                continue

        # newlines
        if token := scan(NEWLINE_REGEX, 'newline'):
            push(Node.from_token(token))
            continue

        # block comment open
        if BLOCK_OPEN_REGEX and kwargs.get('block', None) and not (triple_quotes and block.type == 'block'):
            if token := scan(BLOCK_OPEN_REGEX, 'open'):
                push(Block(type_='block'))
                push(Node.from_token(token))
                continue

        # block comment close
        if BLOCK_CLOSE_REGEX and block.type == 'block' and kwargs.get('block', None):
            if token := scan(BLOCK_CLOSE_REGEX, 'close'):
                try:
                    newline = token.match.groups()[0]
                except LookupError:
                    newline = ''
                push(Node.from_token(token, newline))
                pop()
                continue

        # line comment
        if LINE_REGEX and block.type != 'block' and kwargs.get('line', None):
            if token := scan(LINE_REGEX, 'line'):
                push(Node.from_token(token))
                continue

        # Plain text (skip 'C' since some languages use 'C' to start comments)
        if token := scan(re.compile(r'^[a-zABD-Z0-9\t ]+'), 'text'):
            push(Node.from_token(token))
            continue

        push(Node(type_='text', value=consume(remaining[0])))

    return cst
