
from typing import List

"""
Challenge: Subsets

Given an integer array `nums` of **unique** elements, return all possible subsets (the power set).

The solution set must not contain duplicate subsets. You can return the solution in any order.

Example:
Input: nums = [1,2,3]
Output: [[],[1],[2],[1,2],[3],[1,3],[2,3],[1,2,3]]

Technique:
This is a classic **Backtracking** problem. You can think of it as a decision tree. For each number in `nums`, you have two choices: either **include** it in the current subset or **don't include** it.
"""

def subsets(nums: List[int]) -> List[List[int]]:
    # Your implementation here
    pass

# --- Tests ---
def run_tests():
    test_cases = [
        ([1,2,3], [[],[1],[2],[3],[1,2],[1,3],[2,3],[1,2,3]]),
        ([0], [[],[0]]),
    ]

    for i, (nums, expected) in enumerate(test_cases):
        result = subsets(nums)
        # Sort the results for consistent comparison
        sorted_result = sorted([sorted(sub) for sub in result])
        sorted_expected = sorted([sorted(sub) for sub in expected])
        
        if sorted_result == sorted_expected:
            print(f"Test Case {i + 1}: PASSED")
        else:
            print(f"Test Case {i + 1}: FAILED. Expected {sorted_expected}, got {sorted_result}")

if __name__ == "__main__":
    run_tests()
