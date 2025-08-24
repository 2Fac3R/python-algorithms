
"""
Challenge: Search Insert Position

Given a sorted array of distinct integers and a target value, return the index if the target is found. If not, return the index where it would be if it were inserted in order.

You must write an algorithm with O(log n) runtime complexity.

Technique:
This is a variation of **Binary Search**. The logic is nearly identical, but you need to consider what the state of the `left` and `right` pointers means when the loop terminates. The `left` pointer will end up at the exact position where the target should be inserted.

Instructions:
1. Read the theory on Binary Search in `training/techniques/07_binary_search.md`.
2. Implement the `search_insert` function below.
3. Run this file to test your solution.
"""
from typing import List


def search_insert(nums: List[int], target: int) -> int:
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
    return left

# --- Tests ---


def run_tests():
    test_cases = [
        ([1, 3, 5, 6], 5, 2),
        ([1, 3, 5, 6], 2, 1),
        ([1, 3, 5, 6], 7, 4),
        ([1, 3, 5, 6], 0, 0),
        ([1], 0, 0),
    ]

    for i, (nums, target, expected) in enumerate(test_cases):
        result = search_insert(nums, target)
        if result == expected:
            print(f"Test Case {i + 1}: PASSED")
        else:
            print(
                f"Test Case {i + 1}: FAILED. Expected {expected}, got {result}")


if __name__ == "__main__":
    run_tests()
