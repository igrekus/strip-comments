import re
from dataclasses import dataclass

__all__ = [
    'Block',
    'Node',
    'Token',
]


@dataclass
class Token:
    type_: str
    first_match: str | None
    match: re.Match

    @property
    def type(self):
        return self.type_


class Node:

    def __init__(self, type_=None, value=None, match=None, newline=''):
        self.type = type_
        self.value = value if value else None
        self.match = match if match else None
        self.newline = newline or ''

    @property
    def is_protected(self):
        return bool(self.match) and self.match[1] == '!'


class Block(Node):

    def __init__(self, *args, nodes=None, **kwargs):
        super().__init__(*args, **kwargs)
        self.nodes = nodes if nodes else []

    def push(self, other):
        self.nodes.append(other)

    @property
    def is_protected(self):
        return len(self.nodes) > 0 and self.nodes[0].is_protected
