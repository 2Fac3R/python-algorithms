
"""
Challenge: Binary Search

Given an array of integers `nums` which is sorted in ascending order, and an integer `target`, write a function to search for `target` in `nums`. If `target` exists, then return its index. Otherwise, return -1.

You must write an algorithm with O(log n) runtime complexity.

Technique:
This is the direct implementation of the **Binary Search** algorithm. It requires careful management of the `left`, `right`, and `mid` pointers to correctly narrow down the search space.

Instructions:
1. Read the theory on Binary Search in `training/techniques/07_binary_search.md`.
2. Implement the `search` function below.
3. Run this file to test your solution.
"""
from typing import List


def search(nums: List[int], target: int) -> int:
    left = 0
    right = len(nums) - 1

    while left <= right:
        # mid == target
        mid = left + (right - left) // 2
        if nums[mid] == target:
            return mid
        # left < target entonces buscar en la derecha
        elif nums[mid] < target:
            left = mid + 1
        # right > target entonces buscar en la izquierda
        elif nums[mid] > target:
            right = mid - 1
    return -1

# --- Tests ---


def run_tests():
    test_cases = [
        ([-1, 0, 3, 5, 9, 12], 9, 4),
        ([-1, 0, 3, 5, 9, 12], 2, -1),
        ([5], 5, 0),
        ([5], -5, -1),
    ]

    for i, (nums, target, expected) in enumerate(test_cases):
        result = search(nums, target)
        if result == expected:
            print(f"Test Case {i + 1}: PASSED")
        else:
            print(
                f"Test Case {i + 1}: FAILED. Expected {expected}, got {result}")


if __name__ == "__main__":
    run_tests()
