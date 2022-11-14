from typing import Any
from Array import Array


class Grid(object):
    """Represents a two-dimensional array."""

    def __init__(self, rows: int, columns: int, fill_value: Array = None):
        """
        Args:
            rows (int): number of rows
            columns (int): number of columns
            fill_value (Array, optional): array value. Defaults to None.
        """
        self.data = Array(rows)
        for row in range(rows):
            self.data[row] = Array(columns, fill_value)

    def get_height(self) -> int:
        """
        Returns the number of rows.
        >>> matrix = Grid(3, 1)
        >>> matrix.get_height()
        3
        """
        return len(self.data)

    def get_width(self) -> int:
        """
        Returns the number of columns.
        >>> matrix = Grid(1, 3)
        >>> matrix.get_width()
        3
        """
        return len(self.data[0])

    def __getitem__(self, index) -> Any:
        """
        Supports two-dimensional indexing with [row][column].
        >>> matrix = Grid(3, 3)
        >>> for row in range(matrix.get_height()):
        ...     for column in range(matrix.get_width()):
        ...         matrix[row][column] = row * column
        >>> print(matrix.__getitem__(1))
        [0, 1, 2]
        >>> matrix.__getitem__(1)[2]
        2
        >>> matrix[1][2]
        2
        """
        return self.data[index]

    def __str__(self) -> str:
        """
        Returns a string representation of the grid.
        >>> matrix = Grid(3, 3)
        >>> for row in range(matrix.get_height()):
        ...     for column in range(matrix.get_width()):
        ...         matrix[row][column] = row * column
        >>> print(matrix.__str__())
        0 0 0 
        0 1 2 
        0 2 4 
        <BLANKLINE>
        >>> print(matrix)
        0 0 0 
        0 1 2 
        0 2 4 
        <BLANKLINE>
        """
        result = ""

        for row in range(self.get_height()):
            for col in range(self.get_width()):
                result += str(self.data[row][col]) + " "
            result += "\n"

        return str(result)

    def transpose(self) -> None:
        """
        The transpose of a matrix is found by interchanging 
        its rows into columns or columns into rows.
        >>> matrix = Grid(3, 2)
        >>> for row in range(matrix.get_height()):
        ...     for column in range(matrix.get_width()):
        ...         matrix[row][column] = row * column
        >>> print(matrix)
        0 0 
        0 1 
        0 2 
        <BLANKLINE>
        >>> matrix.transpose()
        >>> print(matrix)
        0 0 0 
        0 1 2 
        <BLANKLINE>
        """
        self.data = list(zip(*self))


if __name__ == '__main__':
    from doctest import testmod
    testmod()
