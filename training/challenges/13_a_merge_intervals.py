
from typing import List

"""
Challenge: Merge Intervals

Given an array of `intervals` where `intervals[i] = [start_i, end_i]`, merge all overlapping intervals, and return an array of the non-overlapping intervals that cover all the intervals in the input.

Example:
Input: intervals = [[1,3],[2,6],[8,10],[15,18]]
Output: [[1,6],[8,10],[15,18]]
Explanation: Since intervals [1,3] and [2,6] overlap, merge them into [1,6].

Technique:
This is the classic **Intervals** problem. The key is to first sort the intervals by their start times. Then, iterate through the sorted intervals and merge any that overlap with the last interval in your result list.
"""

def merge(intervals: List[List[int]]) -> List[List[int]]:
    # Your implementation here
    pass

# --- Tests ---
def run_tests():
    test_cases = [
        ([[1,3],[2,6],[8,10],[15,18]], [[1,6],[8,10],[15,18]]),
        ([[1,4],[4,5]], [[1,5]]),
        ([[1,4],[2,3]], [[1,4]]),
    ]

    for i, (intervals, expected) in enumerate(test_cases):
        result = merge(intervals)
        if result == expected:
            print(f"Test Case {i + 1}: PASSED")
        else:
            print(f"Test Case {i + 1}: FAILED. Expected {expected}, got {result}")

if __name__ == "__main__":
    run_tests()
