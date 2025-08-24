
from typing import List

"""
Challenge: Single Number

Given a **non-empty** array of integers `nums`, every element appears twice except for one. Find that single one.

You must implement a solution with a linear runtime complexity and use only constant extra space.

Example:
Input: nums = [4,1,2,1,2]
Output: 4

Technique:
This is the most classic use case for the **XOR (`^`) bitwise operator**. The properties of XOR allow you to cancel out all the duplicate numbers, leaving only the unique one.
"""

def singleNumber(nums: List[int]) -> int:
    # Your implementation here
    pass

# --- Tests ---
def run_tests():
    test_cases = [
        ([2,2,1], 1),
        ([4,1,2,1,2], 4),
        ([1], 1),
    ]

    for i, (nums, expected) in enumerate(test_cases):
        result = singleNumber(nums)
        if result == expected:
            print(f"Test Case {i + 1}: PASSED")
        else:
            print(f"Test Case {i + 1}: FAILED. Expected {expected}, got {result}")

if __name__ == "__main__":
    run_tests()
