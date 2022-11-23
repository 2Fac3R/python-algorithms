from typing import List


def bubble_sort(list: List[int]) -> List[int]:
    """Bubble Sort - O(n^2)

    https://en.wikipedia.org/wiki/Bubble_sort

    Sorting by swaping elements.

    Args:
        list (List[int]): a collection with comparable items

    Returns:
        List[int]: sorted collection

    Tests:
        >>> collection = [30, 96, 73, 75, 98, 14, 35, 63, 42, 38]
        >>> print(bubble_sort(collection))
        [14, 30, 35, 38, 42, 63, 73, 75, 96, 98]
    """
    n: int = len(list)

    for i in range(n):
        for j in range(0, n - i - 1):
            if list[j] > list[j + 1]:
                list[j], list[j + 1] = list[j + 1], list[j]  # swap
    return list


if __name__ == '__main__':
    from doctest import testmod
    testmod()
