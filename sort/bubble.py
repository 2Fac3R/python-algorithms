from typing import List


def bubble(list: List[int]) -> List[int]:
    """Bubble Sort

    Sorting by swaping elements.
    Time complexity O(n) * O(n) = O(n * n) = O(n^2).

    Args:
        list (List[int]): a collection with comparable items

    Returns:
        List[int]: sorted collection 
    """
    n: int = len(list)

    for i in range(n):
        for j in range(0, n - i - 1):
            if list[j] > list[j + 1]:
                list[j], list[j + 1] = list[j + 1], list[j]
    return list


if __name__ == '__main__':
    import random

    n: int = int(input('Enter list length: '))

    list: List[int] = [random.randint(0, 100) for i in range(n)]
    print(list)

    sorted_list: List[int] = bubble(list)
    print(sorted_list)
