from typing import Any


class Node():
    def __init__(self, data: Any = None, next=None):
        """Singly Linked Node

        Args:
            data (Any, optional): value of the node. Defaults to None.
            next (Node, optional): a pointer to the next node. Defaults to None.
        """
        self.data = data
        self.next = next

    def __repr__(self) -> str:
        """
        Returns a string representation of the node.
        >>> Node(10).__repr__()
        'Node(10)'
        """
        return f"Node({self.data})"


class DoubleNode(object):
    def __init__(self, data: Any = None, next=None, previous=None):
        """Doubly Linked Node

        Args:
            data (Any, optional): value of the node. Defaults to None.
            next (Node, optional): a pointer to the next node. Defaults to None.
            previous (Node, optional): a pointer to the previous node. Defaults to None.
        """
        self.data = data
        self.next = next
        self.previous = previous


if __name__ == '__main__':
    from doctest import testmod
    testmod()
