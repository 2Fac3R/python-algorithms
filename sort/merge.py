from typing import List


def merge_sort(list: List[int]) -> List[int]:
    """Merge Sort

    Sorting by merging sublists.
    Time complexity O(n log n).
    1. Divide the unsorted list into n sublists, each containing one element.
    2. Repeatedly merge sublists to produce new sorted sublists until there is only one sublist remaining.

    Args:
        list (List[int]): a collection with comparable items

    Returns:
        List[int]: sorted collection
    """
    if len(list) > 1:
        middle = len(list) // 2
        left = list[:middle]
        right = list[middle:]

        # recursive call on each half
        merge_sort(left)
        merge_sort(right)

        # Iterators to traverse the two sublists
        i: int = 0
        j: int = 0
        # Iterator for main list
        k: int = 0

        while i < len(left) and j < len(right):
            if left[i] < right[j]:
                list[k] = left[i]
                i += 1
            else:
                list[k] = right[j]
                j += 1

            k += 1

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
    import random

    n: int = int(input('Enter list length: '))

    list: List[int] = [random.randint(0, 100) for i in range(n)]
    print(list)

    sorted_list: List[int] = merge_sort(list)
    print(sorted_list)
