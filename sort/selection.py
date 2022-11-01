from typing import List


def selection(list: List[int]) -> List[int]:
    """Selection Sort

    Sorting by finding min_index.
    Time complexity O(n) * O(n) = O(n * n) = O(n^2).

    Args:
        list (List[int]): a collection with comparable items

    Returns:
        List[int]: sorted collection
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
    import random

    n: int = int(input('Enter list length: '))

    list: List[int] = [random.randint(0, 100) for i in range(n)]
    print(list)

    sorted_list: List[int] = selection(list)
    print(sorted_list)
