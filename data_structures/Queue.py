from Node import DoubleNode as Node


class Queue:
    """Represents a Queue."""

    def __init__(self):
        self.head = None
        self.tail = None
        self.count = 0

    def enqueue(self, data) -> None:
        """
        Adds an element to the queue.

        >>> food = Queue()
        >>> food.enqueue('eggs')
        >>> food.enqueue('ham')
        >>> food.enqueue('spam')
        >>> print(food.head.data)
        eggs
        >>> print(food.head.next.data)
        ham
        >>> print(food.tail.data)
        spam
        """
        new_node = Node(data, None, None)

        if self.head is None:
            self.head = new_node
            self.tail = self.head
        else:
            new_node.previous = self.tail
            self.tail.next = new_node
            self.tail = new_node

        self.count += 1

    def dequeue(self) -> Node:
        """
        Removes an element from the queue.
        >>> food = Queue()
        >>> food.enqueue('eggs')
        >>> food.enqueue('ham')
        >>> food.enqueue('spam')
        >>> food.dequeue().data
        'eggs'
        >>> print(food.head.data)
        ham
        """
        current = self.head

        if self.count == 1:
            self.count -= 1
            self.head = None
            self.tail = None
        elif self.count > 1:
            self.head = self.head.next
            self.head.previous = None
            self.count -= 1

        return current


if __name__ == '__main__':
    from doctest import testmod
    testmod()
