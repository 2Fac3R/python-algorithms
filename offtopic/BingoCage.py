# Book: Fluent Python. Example 7-8
from random import shuffle


class BingoCage:
    """A BingoCage does one thing: picks items from a shuffled list.

    Tests:
        Initialize a BingoCage with a list of items:
        >>> bingo = BingoCage(['apple', 'banana', 'cherry'])
        >>> callable(bingo)
        True

        Pick items from the BingoCage:
        >>> bingo.pick() in ['apple', 'banana', 'cherry']
        True

        After picking items, the BingoCage should have fewer items:
        >>> len(bingo._items) < 3
        True
    """

    def __init__(self, items: list) -> None:
        self._items = list(items)
        shuffle(self._items)

    def pick(self):
        try:
            return self._items.pop()
        except IndexError:
            raise LookupError('pick from empty BingoCage')

    def __call__(self):
        return self.pick()


if __name__ == '__main__':
    from doctest import testmod
    testmod()
