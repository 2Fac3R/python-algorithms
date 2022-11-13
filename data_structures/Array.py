from typing import Any


class Array(object):
    """Represents an array."""

    def __init__(self, capacity: int, fill_value: Any = None):
        """
        Args:
            capacity (int): static size of the array.
            fill_value (Any, optional): value at each position. Defaults to None.
        """
        self.items = list()
        for i in range(capacity):
            self.items.append(fill_value)

    def __len__(self) -> int:
        """
        Returns capacity of the array.
        >>> myList = [1, 5, 2, 3, 4]
        >>> myArray = Array(5, myList)
        >>> len(myArray)
        5
        """
        return len(self.items)

    def __str__(self) -> str:
        """
        Returns string representation of the array.
        >>> myList = [1, 5, 2, 3, 4]
        >>> myArray = Array(3, myList)
        >>> print(myArray)
        [[1, 5, 2, 3, 4], [1, 5, 2, 3, 4], [1, 5, 2, 3, 4]]
        """
        return str(self.items)

    def __iter__(self) -> Any:
        """
        Supports traversal with a for loop.
        >>> myList = [1, 5, 2, 3, 4]
        >>> myArray = Array(3, myList)
        >>> for item in myArray:
        ...     item
        [1, 5, 2, 3, 4]
        [1, 5, 2, 3, 4]
        [1, 5, 2, 3, 4]
        """
        return iter(self.items)

    def __getitem__(self, index) -> Any:
        """
        Subscrit operator for access at index.
        >>> myList = [1, 5, 2, 3, 4]
        >>> myArray = Array(5, myList)
        >>> myArray[1]
        [1, 5, 2, 3, 4]
        """
        return self.items[index]

    def __setitem__(self, index, new_item) -> None:
        """
        Subscript operator for replacement at index.
        >>> myList = [1, 5, 2, 3, 4]
        >>> myArray = Array(5, myList)
        >>> myArray[1] = []
        >>> myArray[1]
        []
        """
        self.items[index] = new_item

    def __sumItems__(self) -> int:
        """
        Returns the sum of all items.
        >>> myList = [1, 5, 2, 3, 4]
        >>> myArray = Array(5, myList)
        >>> myArray.__sumItems__()
        15
        """
        return sum(self.items.__iter__().__next__())


if __name__ == '__main__':
    from doctest import testmod
    testmod()
