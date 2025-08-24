
from typing import List

"""
Challenge: Insert Interval

You are given an array of non-overlapping intervals `intervals` where `intervals[i] = [start_i, end_i]` represent the start and the end of the ith interval and `intervals` is sorted in ascending order by `start_i`. You are also given an interval `newInterval = [start, end]` that represents the start and end of another interval.

Insert `newInterval` into `intervals` such that `intervals` is still sorted in ascending order by `start_i` and `intervals` still does not have any overlapping intervals (merge if necessary).

Return `intervals` after the insertion.

Example:
Input: intervals = [[1,3],[6,9]], newInterval = [2,5]
Output: [[1,5],[6,9]]

Technique:
This is a variation of the merge intervals pattern. Since the initial list is already sorted, you don't need to sort it again. The key is to iterate through the list and build a new result list by handling three cases:
1. The current interval comes entirely before `newInterval`.
2. The current interval overlaps with `newInterval`.
3. The current interval comes entirely after `newInterval`.
"""

def insert(intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
    # Your implementation here
    pass

# --- Tests ---
def run_tests():
    test_cases = [
        ([[1,3],[6,9]], [2,5], [[1,5],[6,9]]),
        ([[1,2],[3,5],[6,7],[8,10],[12,16]], [4,8], [[1,2],[3,10],[12,16]]),
        ([], [5,7], [[5,7]]),
        ([[1,5]], [2,3], [[1,5]]),
    ]

    for i, (intervals, new, expected) in enumerate(test_cases):
        result = insert(intervals, new)
        if result == expected:
            print(f"Test Case {i + 1}: PASSED")
        else:
            print(f"Test Case {i + 1}: FAILED. Expected {expected}, got {result}")

if __name__ == "__main__":
    run_tests()
