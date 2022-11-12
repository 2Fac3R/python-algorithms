from typing import Any
from Node import Node


class Stack:
    """Represents a Stack"""

    def __init__(self):
        self.top = None
        self.size = 0

    def push(self, data: Any):
        """Appends an element on top

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

    def pop(self):
        """
        Removes and returns the element on top.
        >>> myStack = Stack()
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
            return "The stack is empty"

    def peek(self):
        """
        Returns the top node data.
        >>> myStack = Stack()
        >>> myStack.push("item")
        >>> myStack.push("item 2")
        >>> myStack.peek()
        'item 2'
        """
        if self.top:
            return self.top.data
        else:
            return "The stack is empty"

    def clear(self):
        """
        Clears the stack.
        >>> myStack = Stack()
        >>> myStack.push("item")
        >>> myStack.push("item 2")
        >>> myStack.clear()
        >>> myStack.peek()
        'The stack is empty'
        """
        while self.top:
            self.pop()

    def __iter__(self):
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
