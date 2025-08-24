
"""
Challenge: Two Sum

Given an array of integers `nums` and an integer `target`, return indices of the two numbers such that they add up to `target`.

You may assume that each input would have exactly one solution, and you may not use the same element twice.

You can return the answer in any order.
"""
from typing import List


def two_sum(nums: List[int], target: int) -> List[int]:
    hashmap: dict[int, int] = {}

    for index, num in enumerate(nums):
        result = target - num
        if result in hashmap:
            return [index, hashmap[result]]
        hashmap[num] = index

    return []


# --- Tests ---
def run_tests():
    test_cases = [
        ([2, 7, 11, 15], 9, [0, 1]),
        ([3, 2, 4], 6, [1, 2]),
        ([3, 3], 6, [0, 1]),
    ]

    for i, (nums, target, expected) in enumerate(test_cases):
        result = two_sum(nums, target)
        # Sort the result to handle different orderings
        if sorted(result) == sorted(expected):
            print(f"Test Case {i + 1}: PASSED")
        else:
            print(
                f"Test Case {i + 1}: FAILED. Expected {expected}, got {result}")


if __name__ == "__main__":
    run_tests()
