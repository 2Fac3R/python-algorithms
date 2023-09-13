from typing import List


def insertion_sort(list: List[int]) -> List[int]:
    """Insertion Sort - O(n^2)

    https://en.wikipedia.org/wiki/Insertion_sort

    Sorting by inserting the least value in every iteration.

    Args:
        list (List[int]): a collection with comparable items

    Returns:
        List[int]: sorted collection

    Tests:
        >>> collection = [79, 53, 10, 85, 13, 60, 11, 69, 99, 56]
        >>> print(insertion_sort(collection))
        [10, 11, 13, 53, 56, 60, 69, 79, 85, 99]
    """
    for i in range(1, len(list)):
        current_value = list[i]
        current_position = i

        while current_position > 0 and list[current_position - 1] > current_value:
            list[current_position] = list[current_position - 1]
            current_position -= 1

        list[current_position] = current_value

    return list


if __name__ == '__main__':
    from doctest import testmod
    testmod()
