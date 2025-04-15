def factorial(n: int) -> int:
    """Return the factorial of n

    Args:
        n (int): a number

    Raises:
        ValueError: Number should not be negative.

    Returns:
        int: the factorial of n

    Tests:
        >>> factorial(0)
        1
        >>> factorial(1)
        1
        >>> factorial(7)
        5040
        >>> factorial(-1)
        Traceback (most recent call last):
        ...
        ValueError: Number should not be negative.
        >>> [factorial(i) for i in range(10)]
        [1, 1, 2, 6, 24, 120, 720, 5040, 40320, 362880]
    """
    if n < 0:
        raise ValueError("Number should not be negative.")

    if n in (0, 1):
        return 1

    return n * factorial(n - 1)


if __name__ == '__main__':
    from doctest import testmod
    testmod()
