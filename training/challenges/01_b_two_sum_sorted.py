
"""
Challenge: Two Sum II - Input Array Is Sorted

Given a 1-indexed array of integers `numbers` that is already sorted in non-decreasing order,
find two numbers such that they add up to a specific `target` number.

Return the indices of the two numbers (1-indexed) as an integer array `[index1, index2]` of size 2.

You may assume that each input would have exactly one solution and you may not use the same element twice.
Your solution must use only constant extra space.

Technique:
This problem is a perfect fit for the **Two Pointers** technique on a sorted array.
By starting with pointers at both ends, you can intelligently move them based on whether the
current sum is too small or too large.

Instructions:
1. Read the theory on Two Pointers in `training/techniques/01_two_pointers.md`.
2. Implement the `two_sum_sorted` function below.
3. Run this file using `python training/challenges/01_b_two_sum_sorted.py` to test your solution.
"""
from typing import List

# This is the standard and most efficient approach for sorted arrays.


def two_sum_sorted(numbers: List[int], target: int) -> List[int]:
    left, right = 0, len(numbers) - 1

    while left < right:
        current_sum = numbers[left] + numbers[right]
        if current_sum == target:
            return [left + 1, right + 1]  # Found! (1-indexed)
        elif current_sum < target:  # Sum too small, need a larger number
            left += 1
        else:  # current_sum > target, sum too large, need a smaller number
            right -= 1
    return []  # Should not be reached given problem constraints


# --- Tests ---
def run_tests():
    test_cases = [
        ([2, 7, 11, 15], 9, [1, 2]),
        ([2, 3, 4], 6, [1, 3]),
        ([-1, 0], -1, [1, 2]),
        ([5, 25, 75], 100, [2, 3]),
    ]

    for i, (numbers, target, expected) in enumerate(test_cases):
        result = two_sum_sorted(numbers, target)
        if result == expected:
            print(f"Test Case {i + 1}: PASSED")
        else:
            print(
                f"Test Case {i + 1}: FAILED. Expected {expected}, got {result}")


if __name__ == "__main__":
    run_tests()
