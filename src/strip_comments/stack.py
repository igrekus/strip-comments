from typing import Tuple

from strip_comments.models import Block, Node

__all__ = [
    'Stack'
]


class Stack:

    def __init__(self):
        self._cst = Block(type_='root', nodes=[])
        self._stack = [self._cst]
        self._current_block = self._cst
        self._prev: Node | None = None

    def push(self, node: Node | Block) -> None:
        if self._prev and self._prev.type == 'text' and node.type == 'text':
            self._prev.value += node.value
            return

        self._current_block.push(node)
        if hasattr(node, 'nodes'):
            self._stack.append(node)
            self._current_block = node
        self._prev = node

    def pop(self) -> None:
        if self._current_block.type == 'root':
            raise ValueError('Unclosed block comment in the input source')

        self._stack.pop()
        self._current_block = self._stack[len(self._stack) - 1]

    @property
    def cst(self) -> Block:
        return self._cst

    @property
    def cur_block_type(self) -> str:
        return self._current_block.type

    @property
    def is_prev_exists(self) -> bool:
        return bool(self._prev)

    @property
    def prev_value(self) -> str | None:
        return self._prev.value

    @property
    def is_block(self):
        return self.cur_block_type == 'block'
