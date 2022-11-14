from typing import Any
from Node import Node


class Stack:
    """Represents a Stack."""

    def __init__(self):
        self.top = None
        self.size = 0

    def push(self, data: Any) -> None:
        """
        Appends an element on top

        Args:
            data (Any): data to append
        Tests:
        >>> myStack = Stack()
        >>> myStack.push("item")
        >>> myStack.push("item 2")
        >>> myStack.peek()
        'item 2'
        """
        node = Node(data)

        if self.top:
            node.next = self.top
            self.top = node
        else:
            self.top = node

        self.size += 1

    def pop(self) -> Any:
        """
        Removes and returns the element on top.
        >>> myStack = Stack()
        >>> myStack.pop()
        Traceback (most recent call last):
        ...
        Exception: The stack is empty
        >>> myStack.push("item")
        >>> myStack.push("item 2")
        >>> myStack.push("item 3")
        >>> myStack.pop()
        'item 3'
        >>> myStack.peek()
        'item 2'
        """
        if self.top:
            data = self.top.data
            self.size -= 1

            if self.top.next:
                self.top = self.top.next
            else:
                self.top = None

            return data
        else:
            raise Exception("The stack is empty")

    def is_empty(self) -> bool:
        """
        Returns True if stack is empty, or False otherwise.
        >>> myStack = Stack()
        >>> myStack.is_empty()
        True
        >>> myStack.push("item")
        >>> myStack.is_empty()
        False
        >>> myStack.pop()
        'item'
        >>> myStack.is_empty()
        True
        """
        return not self.top

    def peek(self) -> Any:
        """
        Returns the top node data.
        >>> myStack = Stack()
        >>> myStack.peek()
        Traceback (most recent call last):
        ...
        Exception: The stack is empty
        >>> myStack.push("item")
        >>> myStack.push("item 2")
        >>> myStack.peek()
        'item 2'
        """
        if self.top:
            return self.top.data
        else:
            raise Exception("The stack is empty")

    def clear(self) -> None:
        """
        Clears the stack.
        >>> myStack = Stack()
        >>> myStack.push("item")
        >>> myStack.push("item 2")
        >>> myStack.clear()
        >>> myStack.peek()
        Traceback (most recent call last):
        ...
        Exception: The stack is empty
        """
        while self.top:
            self.pop()

    def search(self, data: Any) -> Node:
        """
        Returns node if found, or None otherwise.
        >>> myStack = Stack()
        >>> myStack.push("item")
        >>> myStack.push("item 2")
        >>> myStack.push("item 3")
        >>> myStack.search("item 2")
        Node(item 2)
        >>> myStack.search("item 4")
        """
        current = self.top
        while current:
            if current.data == data:
                return current
            current = current.next
        return None

    def __contains__(self, data: Any) -> bool:
        """
        Returns True if found, or False otherwise.
        >>> myStack = Stack()
        >>> myStack.push("item")
        >>> myStack.push("item 2")
        >>> myStack.push("item 3")
        >>> "item 2" in myStack
        True
        >>> "item 4" in myStack
        False
        """
        current = self.top
        while current:
            if current.data == data:
                return True
            current = current.next
        return False

    def __iter__(self) -> Any:
        """
        This function is intended for iterators to access
        and iterate through data inside linked list.
        >>> myStack = Stack()
        >>> myStack.push("item")
        >>> myStack.push("item 2")
        >>> myStack.push("item 3")
        >>> for item in myStack:
        ...     item
        'item 3'
        'item 2'
        'item'
        """
        node = self.top
        while node:
            yield node.data
            node = node.next


if __name__ == '__main__':
    from doctest import testmod
    testmod()
