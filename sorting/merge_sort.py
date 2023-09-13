from typing import List


def merge_sort(list: List[int]) -> List[int]:
    """Merge Sort (Recursive) - O(n log n)

    https://en.wikipedia.org/wiki/Merge_sort

    Sorting by merging sublists.
    1. Divide the unsorted list into n sublists, each containing one element.
    2. Repeatedly merge sublists to produce new sorted sublists
       until there is only one sublist remaining.

    Args:
        list (List[int]): a collection with comparable items

    Returns:
        List[int]: sorted collection

    Tests:
        >>> collection = [30, 96, 73, 75, 98, 14, 35, 63, 42, 38]
        >>> collection_2 = [87, 36, 55, 25, 91, 67, 3, 33, 56, 56]
        >>> print(merge_sort([]))
        []
        >>> print(merge_sort([1]))
        [1]
        >>> print(merge_sort(collection))
        [14, 30, 35, 38, 42, 63, 73, 75, 96, 98]
        >>> print(merge_sort(collection_2))
        [3, 25, 33, 36, 55, 56, 56, 67, 87, 91]
    """
    if len(list) > 1:  # Base case. A list of zero or one elements is sorted
        middle = len(list) // 2
        left = list[:middle]
        right = list[middle:]

        # Recursively sort both sublists.
        merge_sort(left)
        merge_sort(right)

        # Iterators to traverse the two sublists
        i: int = 0
        j: int = 0
        # Iterator for main list
        k: int = 0

        # Merging...
        while i < len(left) and j < len(right):
            if left[i] < right[j]:
                list[k] = left[i]
                i += 1
            else:
                list[k] = right[j]
                j += 1

            k += 1

        # Either left or right may have elements left; consume them.
        while i < len(left):
            list[k] = left[i]
            i += 1
            k += 1

        while j < len(right):
            list[k] = right[j]
            j += 1
            k += 1

    return list


if __name__ == '__main__':
    from doctest import testmod
    testmod()
