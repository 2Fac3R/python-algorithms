def fib(i: int) -> int:
    """Fibonacci number

    https://en.wikipedia.org/wiki/Fibonacci_number

    Base cases: fib(0) = 0 and fib(1) = 1
    Recurrence relation: fib(i) = fib(i-1) + fib(i-2)

    Args:
        i (int): a number

    Returns:
        int: fibonacci number

    Tests:
        >>> fib(0)
        0
        >>> fib(1)
        1
        >>> [fib(i) for i in range(10)]
        [0, 1, 1, 2, 3, 5, 8, 13, 21, 34]
    """
    if i in (0, 1):
        return i

    return fib(i - 1) + fib(i - 2)


if __name__ == '__main__':
    from doctest import testmod
    testmod()
