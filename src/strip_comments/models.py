import re
from dataclasses import dataclass, field

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


@dataclass
class Node:
    type_: str
    value: str | None = None
    match: re.Match | None = None
    newline: str = ''

    @property
    def is_protected(self):
        return bool(self.match) and self.match[1] == '!'

    @property
    def type(self):
        return self.type_


@dataclass
class Block(Node):
    nodes: list[Node] = field(default_factory=list)

    def push(self, other):
        self.nodes.append(other)

    @property
    def is_protected(self):
        return len(self.nodes) > 0 and self.nodes[0].is_protected
