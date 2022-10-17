from functools import reduce


class Array(object):
    """Represents an array."""

    def __init__(self, capacity, fill_value=None):
        """
        Args:
            capacity (int): static size of the array.
            fill_value (any, optional): value at each position. Defaults to None.
        """
        self.items = list()
        for i in range(capacity):
            self.items.append(fill_value)

    def __len__(self):
        """Returns capacity of the array."""
        return len(self.items)

    def __str__(self):
        """Returns string representation of the array"""
        return str(self.items)

    def __iter__(self):
        """Supports traversal with a for loop."""
        return iter(self.items)

    def __getitem__(self, index):
        """Subscrit operator for access at index."""
        return self.items[index]

    def __setitem__(self, index, new_item):
        """Subscript operator for replacement at index."""
        self.items[index] = new_item

    def __sumItems__(self):
        """Returns the sum of all items."""
        return sum(self.items.__iter__().__next__())
        # return reduce(lambda a, b: a+b, self.items.__iter__().__next__())


if __name__ == '__main__':
    myList = [1, 5, 2, 3, 4]
    myArray = Array(5, myList)

    # for i in range(len(myArray)):
    #     myArray[i] = i * 3

    # myArray = [i*3 for i in range(len(myArray))]

    # print(len(myArray))
    print(myArray.__sumItems__())
