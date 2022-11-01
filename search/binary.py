def binary(sequence: list, beginning: int, end: int, target: int) -> bool:
    """Binary Search

    Args:
        sequence (list): a collection with comparable items
        beginning (int): position to start looking for
        end (int): final position
        target (int): item value to search

    Returns:
        bool: True if target is found, or False otherwise
    """
    print(
        f'Looking for {target} between {sequence[beginning]} and {sequence[end - 1]}')
    if beginning > end:
        return False

    mid = (beginning + end) // 2

    if sequence[mid] == target:
        return True
    elif sequence[mid] < target:
        return binary(sequence, mid + 1, end, target)
    else:
        return binary(sequence, beginning, mid - 1, target)


if __name__ == '__main__':
    import random

    n: int = int(input('Enter list length: '))
    target: int = int(input('Search: '))

    sequence: list = sorted([random.randint(0, 100)
                             for i in range(n)])

    found: bool = binary(sequence, 0, len(sequence), target)

    print(sequence)
    print(
        f'{target} {"found" if found else "not found"}.')
