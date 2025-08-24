
from typing import List
import heapq

"""
Challenge: Kth Largest Element in an Array

Given an integer array `nums` and an integer `k`, return the `k`th largest element in the array.

Note that it is the `k`th largest element in the sorted order, not the `k`th distinct element.

Example:
Input: nums = [3,2,1,5,6,4], k = 2
Output: 5

Technique:
This is a classic problem for a **Min-Heap**. The goal is to maintain a min-heap of size `k`. The smallest element in this heap (the root) is our candidate for the `k`th largest element overall. When we encounter a new number larger than this candidate, we replace the candidate with the new number.
"""

def findKthLargest(nums: List[int], k: int) -> int:
    # Your implementation here
    pass

# --- Tests ---
def run_tests():
    test_cases = [
        ([3,2,1,5,6,4], 2, 5),
        ([3,2,3,1,2,4,5,5,6], 4, 4),
        ([1], 1, 1),
    ]

    for i, (nums, k, expected) in enumerate(test_cases):
        result = findKthLargest(nums, k)
        if result == expected:
            print(f"Test Case {i + 1}: PASSED")
        else:
            print(f"Test Case {i + 1}: FAILED. Expected {expected}, got {result}")

if __name__ == "__main__":
    run_tests()
