from typing import List


def first_missing_positive(nums: List[int]) -> int:
    """First Missing Positive

    Args:
        nums (List[int]): an unsorted integer array nums

    Returns:
        int: the smallest missing positive integer

    Tests:
        >>> first_missing_positive([1, 2, 0])
        3
        >>> first_missing_positive([3, 4, -1, 1])
        2
        >>> first_missing_positive([7, 8, 9, 11, 12])
        1
    """
    unique = set(nums)
    i = 1

    while i in unique:
        i += 1

    return i


if __name__ == '__main__':
    import doctest
    doctest.testmod()
