
"""
Challenge: Maximum Sum Subarray of Size K

Given an array of integers `arr` and a positive integer `k`, find the maximum sum of a contiguous subarray of size `k`.

Technique:
This is a classic problem for the **Fixed-Size Sliding Window** technique. A brute-force approach would be O(n*k), but with a sliding window, you can achieve O(n).

Instructions:
1. Read the theory on Sliding Window in `training/techniques/02_sliding_window.md`.
2. Implement the `max_subarray_sum` function below.
3. Run this file to test your solution.
"""
from typing import List


def max_subarray_sum(arr: List[int], k: int) -> int:
    pointer, end, sums = 0, len(arr) - 1, {}

    while pointer < end:
        sums[pointer] = sum(arr[pointer: pointer + k])
        pointer += 1

    return max(sums.values())

# --- Tests ---


def run_tests():
    test_cases = [
        ([2, 1, 5, 1, 3, 2], 3, 9),  # 5 + 1 + 3 = 9
        ([2, 3, 4, 1, 5], 2, 7),    # 3 + 4 = 7
        ([1, 1, 1, 1, 1], 1, 1),
        ([10, 20, 5, 15, 30, 5], 4, 70),  # 20 + 5 + 15 + 30 = 70
    ]

    for i, (arr, k, expected) in enumerate(test_cases):
        result = max_subarray_sum(arr, k)
        if result == expected:
            print(f"Test Case {i + 1}: PASSED")
        else:
            print(
                f"Test Case {i + 1}: FAILED. Expected {expected}, got {result}")


if __name__ == "__main__":
    run_tests()
