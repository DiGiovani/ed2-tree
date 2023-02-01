# Type Self was added in Python 3.11. See more details in https://peps.python.org/pep-0673/
from typing import Self


class Root:
    left: Self | None
    right: Self | None
    value: int

    def __init__(self, value: int, left: Self | None, right: Self | None):
        self.value = value
        self.left = left
        self.right = right


class Node(Root):
    parent: Root
    height: int

    def __init__(
        self,
        parent: Root,
        value: int,
        height: int,
        left: Self | None = None,
        right: Self | None = None,
    ):
        self.parent = parent
        self.left = left
        self.right = right
        self.value = value
        self.height = height


class Tree:
    root: Root

    def pre_order(self, node: Root | None):
        node = node if node is not None else self.root

        print(node.value)

        if node.left is not None:
            self.pre_order(node.left)

        if node.right is not None:
            self.pre_order(node.right)

    def in_order(self, node: Root | None):
        node = node if node is not None else self.root

        if node.left is not None:
            self.in_order(node.left)

        print(node.value)

        if node.right is not None:
            self.in_order(node.right)

    def post_order(self, node: Root | None):
        node = node if node is not None else self.root

        if node.left is not None:
            self.post_order(node.left)

        if node.right is not None:
            self.post_order(node.right)

        print(node.value)

    def seek(self, value: int, node: Root | None) -> Root | None:
        node = node if node is not None else self.root

        if node.value < value:
            return self.seek(value, node.left)
        if node.value > value:
            return self.seek(value, node.right)

        return node if node.value == value else None
