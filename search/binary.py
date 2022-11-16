from typing import Any


def binary_search_r(sequence: list, target: int, beginning: int, end: int) -> Any:
    """Binary Search (Recursive) - O(log n)

    https://en.wikipedia.org/wiki/binary_search_algorithm

    Args:
        sequence (list): a sorted collection with comparable items
        target (int): item value to search
        beginning (int): position to start looking for
        end (int): final position

    Returns:
        int | None: target if found, or None otherwise

    Tests:
        >>> sequence = [2, 3, 10, 10, 14, 19, 20, 22, 26, 31, 33, 33, 39, 47]
        >>> n = len(sequence)
        >>> binary_search_r(sequence, 18, n, 0)  # None
        >>> binary_search_r(sequence, 18, 0, n)  # None
        >>> binary_search_r(sequence, 14, 0, n)  # left
        14
        >>> binary_search_r(sequence, 22, 0, n)  # mid
        22
        >>> binary_search_r(sequence, 26, 0, n)  # right
        26
    """
    if beginning > end:
        return None

    mid = (beginning + end) // 2

    if sequence[mid] == target:  # mid
        return sequence[mid]
    elif sequence[mid] > target:  # left
        return binary_search_r(sequence, target, beginning, mid - 1)
    else:  # right
        return binary_search_r(sequence, target, mid + 1, end)


if __name__ == '__main__':
    from doctest import testmod
    testmod()
