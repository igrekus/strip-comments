from typing import Tuple

from strip_comments.models import Block, Node


class Stack:
    def __init__(self, initial: list[Node | Block] | None = None):
        self._stack = list(initial) or []

    def push(self, node: Node | Block, prev, block) -> Tuple[Node | Block, Node | Block]:
        # mutates
        if prev and prev.type == 'text' and node.type == 'text':
            prev.value += node.value
            return prev, block

        block.push(node)
        if hasattr(node, 'nodes'):
            self._stack.append(node)
            block = node
        prev = node
        return prev, block

    def pop(self, block) -> Node | Block:
        if block.type == 'root':
            raise SyntaxError('Unclosed block comment')

        self._stack.pop()
        return self._stack[len(self._stack) - 1]
