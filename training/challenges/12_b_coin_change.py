
from typing import List

"""
Challenge: Coin Change

You are given an integer array `coins` of different denominations and an integer `amount`.

Return the fewest number of coins that you need to make up that amount. If that amount of money cannot be made up by any combination of the coins, return -1.

You may assume that you have an infinite number of each kind of coin.

Example:
Input: coins = [1,2,5], amount = 11
Output: 3
Explanation: 11 = 5 + 5 + 1

Technique:
This is a classic **Dynamic Programming** problem. The goal is to find the minimum number of coins for each amount from 1 up to the target `amount`. The solution for a given `amount` can be built upon the solutions for smaller amounts.
"""

def coinChange(coins: List[int], amount: int) -> int:
    # Your implementation here
    pass

# --- Tests ---
def run_tests():
    test_cases = [
        ([1,2,5], 11, 3),
        ([2], 3, -1),
        ([1], 0, 0),
        ([1], 1, 1),
    ]

    for i, (coins, amount, expected) in enumerate(test_cases):
        result = coinChange(coins, amount)
        if result == expected:
            print(f"Test Case {i + 1}: PASSED")
        else:
            print(f"Test Case {i + 1}: FAILED. Expected {expected}, got {result}")

if __name__ == "__main__":
    run_tests()
