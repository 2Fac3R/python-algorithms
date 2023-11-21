"""
    Book: Fluent Python by Luciano Ramalho
    Example 1-2. A simple two dimensional vector class

    Tests:
    >>> v1 = Vector(2, 4)
    >>> v2 = Vector(2, 1)
    >>> v1 + v2
    Vector(4, 5)
    >>> v = Vector(3, 4)
    >>> abs(v)
    5.0
    >>> v * 3
    Vector(9, 12)
    >>> abs(v * 3)
    15.0
"""
import math


class Vector:
    def __init__(self, x: float = 0, y: float = 0) -> None:
        self.x = x
        self.y = y

    def __repr__(self) -> str:
        return f'Vector({self.x!r}, {self.y!r})'

    def __abs__(self) -> float:
        return math.hypot(self.x, self.y)

    def __bool__(self) -> bool:
        # return bool(abs(self))
        return bool(self.x or self.y)

    def __add__(self, other: 'Vector') -> 'Vector':
        x = self.x + other.x
        y = self.y + other.y
        return Vector(x, y)

    def __mul__(self, scalar: float) -> 'Vector':
        return Vector(self.x * scalar, self.y * scalar)


if __name__ == '__main__':
    import doctest
    doctest.testmod()
