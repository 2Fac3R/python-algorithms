from typing import Deque, List


def daily_temperatures(temperatures: List[int]) -> List[int]:
    """Daily Temperatures

    Given an array of integers temperatures that represents the daily temperatures,
    return an array answer such that answer[i] is the number of days
    you have to wait after the ith day to get a warmer temperature.

    If there is no future day for which this is possible, keep answer[i] == 0 instead.

    Args:
        temperatures (List[int]): list of integers temperatures that represents the daily temperatures

    Returns:
        List[int]: a list answer

    Tests:
        >>> daily_temperatures([73, 74, 75, 71, 69, 72, 76, 73])
        [1, 1, 4, 2, 1, 1, 0, 0]
        >>> daily_temperatures([30, 40, 50, 60])
        [1, 1, 1, 0]
        >>> daily_temperatures([30, 60, 90])
        [1, 1, 0]
    """
    # Brute Force O(n^2)
    # n: int = len(temperatures)
    # answer: List[int] = [0] * n
    # for i in range(n):
    #     for j in range(i + 1, n):
    #         if temperatures[j] > temperatures[i]:
    #             answer[i] = j - i
    #             break
    # Stack O(2n)
    n: int = len(temperatures)
    answer: List[int] = [0] * n
    stack: Deque = Deque()
    for i in range(n):
        while stack and temperatures[stack[-1]] < temperatures[i]:
            index = stack.pop()
            answer[index] = i-index
        stack.append(i)
    return answer


if __name__ == '__main__':
    from doctest import testmod
    testmod()
