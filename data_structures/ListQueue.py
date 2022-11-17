class ListQueue:
    """Represents a Queue using lists."""

    def __init__(self):
        self.items = []
        self.size = 0

    def enqueue(self, data):
        """
        Adds an element to the queue.
        >>> food = ListQueue()
        >>> food.enqueue('eegs')
        >>> food.enqueue('ham')
        >>> print(food.items[0])
        ham
        """
        self.items.insert(0, data)
        self.size += 1

    def dequeue(self):
        """
        Removes an element from the queue.
        >>> food = ListQueue()
        >>> food.enqueue('eegs')
        >>> food.enqueue('ham')
        >>> food.dequeue()
        'eegs'
        >>> print(food.items)
        ['ham']
        """
        data = self.items.pop()
        self.size -= 1
        return data

    def traverse(self):
        """
        Traverse the queue.
        >>> food = ListQueue()
        >>> food.enqueue('eegs')
        >>> food.enqueue('ham')
        >>> food.enqueue('tomato')
        >>> food.traverse()
        tomato
        ham
        eegs
        """
        for item in self.items:
            print(item)


if __name__ == '__main__':
    from doctest import testmod
    testmod()
