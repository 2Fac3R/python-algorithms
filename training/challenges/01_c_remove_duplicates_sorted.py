
"""
Challenge: Remove Duplicates from Sorted Array

Given an integer array `nums` sorted in non-decreasing order, remove the duplicates **in-place** such that each unique element appears only once. The relative order of the elements should be kept the same.

Since it is impossible to change the length of the array in some languages, you must instead have the result be placed in the first part of the array `nums`. More formally, if there are `k` unique elements after removing the duplicates, then the first `k` elements of `nums` should hold the final result. It does not matter what you leave beyond the first `k` elements.

Return `k` after placing the final result in the first `k` slots of `nums`.

Do not allocate extra space for another array. You must do this by modifying the input array **in-place** with O(1) extra memory.

Technique:
This is a classic use case for the **Fast & Slow Two Pointers** pattern.
- The `slow` pointer (e.g., `insert_index`) keeps track of the position for the next unique element.
- The `fast` pointer scans the array to find new unique elements.
"""
from typing import List

def remove_duplicates(nums: List[int]) -> int:
    # Your implementation here
    pass

# --- Tests ---
def run_tests():
    test_cases = [
        ([1, 1, 2], 2, [1, 2]),
        ([0, 0, 1, 1, 1, 2, 2, 3, 3, 4], 5, [0, 1, 2, 3, 4]),
        ([], 0, []),
        ([1, 2, 3], 3, [1, 2, 3]),
    ]

    for i, (nums, expected_k, expected_nums) in enumerate(test_cases):
        original_nums = list(nums) # Make a copy for the print message
        k = remove_duplicates(nums)
        result_nums = nums[:k]

        if k == expected_k and result_nums == expected_nums:
            print(f"Test Case {i + 1}: PASSED")
        else:
            print(f"Test Case {i + 1}: FAILED. For input {original_nums}, expected k={expected_k} and nums[:k]={expected_nums}, but got k={k} and nums[:k]={result_nums}")

if __name__ == "__main__":
    run_tests()
