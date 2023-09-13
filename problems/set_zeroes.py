from typing import List


def set_zeroes(matrix: List[List[int]]) -> None:
    """Set Zeroes
    Given an m x n integer matrix, if an element is 0, set its entire row and column to 0's.

    Args:
        matrix (List[List[int]]): an m x n integer matrix

    Tests:
        >>> matrix = [[1, 1, 1], [1, 0, 1], [1, 1, 1]]
        >>> set_zeroes(matrix)
        >>> matrix
        [[1, 0, 1], [0, 0, 0], [1, 0, 1]]

        >>> matrix = [[0, 1, 2, 0], [3, 4, 5, 2], [1, 3, 1, 5]]
        >>> set_zeroes(matrix)
        >>> matrix
        [[0, 0, 0, 0], [0, 4, 5, 0], [0, 3, 1, 0]]
    """
    rows_len = len(matrix)
    columns_len = len(matrix[0])
    rows, cols = set(), set()

    # Essentially, we mark the rows and columns that are to be made zero
    for row in range(rows_len):
        for column in range(columns_len):
            if matrix[row][column] == 0:
                rows.add(row)
                cols.add(column)

    # Iterate over the array once again and using the rows and cols sets, update the elements
    for row in range(rows_len):
        for column in range(columns_len):
            if row in rows or column in cols:
                matrix[row][column] = 0


if __name__ == '__main__':
    from doctest import testmod
    testmod()
