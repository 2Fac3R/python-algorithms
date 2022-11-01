def knapsack(capacity: int, weights: list, values: list, n: int) -> int:
    """Knapsack
    https://en.wikipedia.org/wiki/Knapsack_problem

    Returns the maximum value that can be put in a knapsack of a certain capacity,
    whereby each weight has a specific value.

    Args:
        capacity (int): capacity of the knapsack
        values (list): values to put in the knapsack
        weights (list): weights for each value
        n (int): len of values

    Returns:
        int: the maximum value that can be put in a knapsack

    Tests:
        >>> capacity = 50
        >>> values = [60, 100, 120]
        >>> weights = [10, 20, 30]
        >>> n = len(values)
        >>> knapsack(capacity, weights, values, n)
        220

        The result is 220 cause the values of 100 and 120 got the weight of 50
        which is the limit of the capacity.
    """
    if n == 0 or capacity == 0:
        return 0

    if weights[n - 1] > capacity:
        return knapsack(capacity, weights, values, n - 1)

    return max(values[n - 1] + knapsack(capacity - weights[n - 1], weights, values, n - 1),
               knapsack(capacity, weights, values, n - 1))


if __name__ == '__main__':
    import doctest
    doctest.testmod()
