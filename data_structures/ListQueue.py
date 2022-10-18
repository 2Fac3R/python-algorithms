class ListQueue:
    def __init__(self):
        self.items = []
        self.size = 0

    def enqueue(self, data):
        """Adds an element to the queue."""
        self.items.insert(0, data)
        self.size += 1

    def dequeue(self):
        """Removes an element from the queue."""
        data = self.items.pop()
        self.size -= 1
        return data

    def traverse(self):
        """Traverse the queue."""
        for item in self.items:
            print(item)


if __name__ == '__main__':
    food = ListQueue()

    food.enqueue('eegs')
    food.enqueue('ham')
    food.enqueue('spam')

    print(food.items)

    food.dequeue()
    print(food.items)

    food.traverse()
