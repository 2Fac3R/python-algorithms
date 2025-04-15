"""
    Book: Fluent Python by Luciano Ramalho
    Example 1-2. A simple two dimensional vector class
"""


class Vector:
    """
    A simple two-dimensional vector class.

    Methods:
    - __init__: Initialize a vector with x and y coordinates.
    - __repr__: Return a string representation of the vector.
    - __abs__: Return the magnitude of the vector.
    - __bool__: Return True if the vector is non-zero.
    - __add__: Add two vectors.
    - __mul__: Multiply the vector by a scalar.
    """

    def __init__(self, x: float = 0, y: float = 0) -> None:
        """
        Initialize a vector with x and y coordinates.

        >>> v = Vector(3, 4)
        >>> v.x, v.y
        (3, 4)
        """
        self.x = x
        self.y = y

    def __repr__(self) -> str:
        """
        Return a string representation of the vector.

        >>> v = Vector(3, 4)
        >>> repr(v)
        'Vector(3, 4)'
        """
        return f'Vector({self.x!r}, {self.y!r})'

    def __abs__(self) -> float:
        """
        Return the magnitude of the vector.

        >>> v = Vector(3, 4)
        >>> abs(v)
        5.0
        """
        from math import hypot
        return hypot(self.x, self.y)

    def __bool__(self) -> bool:
        """
        Return True if the vector is non-zero.

        >>> v1 = Vector(0, 0)
        >>> bool(v1)
        False
        >>> v2 = Vector(1, 0)
        >>> bool(v2)
        True
        """
        return bool(self.x or self.y)

    def __add__(self, other: 'Vector') -> 'Vector':
        """
        Add two vectors.

        >>> v1 = Vector(2, 4)
        >>> v2 = Vector(2, 1)
        >>> v1 + v2
        Vector(4, 5)
        """
        x = self.x + other.x
        y = self.y + other.y
        return Vector(x, y)

    def __mul__(self, scalar: float) -> 'Vector':
        """
        Multiply the vector by a scalar.

        >>> v = Vector(3, 4)
        >>> v * 3
        Vector(9, 12)
        """
        return Vector(self.x * scalar, self.y * scalar)


if __name__ == '__main__':
    from doctest import testmod
    testmod()
