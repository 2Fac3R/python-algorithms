
from typing import List

"""
Challenge: Implement Merge Sort

Given an array of integers `nums`, sort the array in ascending order using the **Merge Sort** algorithm.

Technique:
Merge Sort is a perfect example of the **Divide and Conquer** paradigm.
1.  **Divide:** Recursively split the array in half until you have arrays of size 1 (the base case).
2.  **Conquer:** The arrays of size 1 are already sorted.
3.  **Combine:** Merge the sorted subarrays back together in the correct order.
"""

def merge_sort(nums: List[int]) -> List[int]:
    # Your implementation here
    pass

# --- Tests ---
def run_tests():
    test_cases = [
        ([5,2,3,1], [1,2,3,5]),
        ([3,1,4,5,2,6], [1,2,3,4,5,6]),
        ([1], [1]),
        ([], []),
    ]

    for i, (nums, expected) in enumerate(test_cases):
        result = merge_sort(nums)
        if result == expected:
            print(f"Test Case {i + 1}: PASSED")
        else:
            print(f"Test Case {i + 1}: FAILED. Expected {expected}, got {result}")

if __name__ == "__main__":
    run_tests()
