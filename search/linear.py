def linear(sequence: list, target: int) -> int:
    """Linear Search - O(n/2)

    https://en.wikipedia.org/wiki/Linear_search

    Args:
        sequence (list): a collection with comparable items
        target (int): item value to search

    Returns:
        int: index of found item, or -1 if item is not found

    Tests:
        >>> linear([], 1)
        -1
        >>> linear([2, 9, 1], 0)
        -1
        >>> linear([2, 9, 1], 1)
        2
    """
    for index, element in enumerate(sequence):
        if element == target:
            return index
    return -1


if __name__ == '__main__':
    import doctest
    doctest.testmod()
