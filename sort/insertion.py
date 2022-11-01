from typing import List


def insertion(list: List[int]) -> List[int]:
    """Insertion Sort

    Sorting by inserting the least value in every iteration.
    Time complexity O(n) * O(n) = O(n * n) = O(n^2).

    Args:
        list (List[int]): a collection with comparable items

    Returns:
        List[int]: sorted collection
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
    import random

    n: int = int(input('Enter list length: '))

    list: List[int] = [random.randint(0, 100) for i in range(n)]
    print(list)

    sorted_list: List[int] = insertion(list)
    print(sorted_list)
