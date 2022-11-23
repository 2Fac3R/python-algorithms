from typing import List


def selection_sort(list: List[int]) -> List[int]:
    """Selection Sort - O(n^2)

    https://en.wikipedia.org/wiki/Selection_sort

    Sorting by finding min_index.

    Args:
        list (List[int]): a collection with comparable items

    Returns:
        List[int]: sorted collection

    Tests:
        >>> collection = [79, 53, 10, 85, 13, 60, 11, 69, 99, 56]
        >>> print(selection_sort(collection))
        [10, 11, 13, 53, 56, 60, 69, 79, 85, 99]
    """
    n: int = len(list)

    for i in range(n):
        min_index = i
        for j in range(i + 1, n):
            # select the minimum element in every iteration
            if list[j] < list[min_index]:
                min_index = j
        # swapping the elements to sort the array
        list[i], list[min_index] = list[min_index], list[i]
    return list


if __name__ == '__main__':
    from doctest import testmod
    testmod()
