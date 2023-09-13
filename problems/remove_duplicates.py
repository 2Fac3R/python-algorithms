def remove_duplicates(dups: list = []) -> list:
    """Remove duplicates

    Args:
        dups (list): original list. Defaults to [].

    Returns:
        list: a list with no duplicates

    Tests:
        >>> remove_duplicates([])
        []
        >>> remove_duplicates([1, 1, 1])
        [1]
        >>> remove_duplicates([1, 3, 6, 2, 1, 2, 8, 0])
        [0, 1, 2, 3, 6, 8]
    """
    return list(set(dups))


if __name__ == '__main__':
    import doctest
    doctest.testmod()
