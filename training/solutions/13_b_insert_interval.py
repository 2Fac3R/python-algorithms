
from typing import List

"""
Solution for: Insert Interval
"""

def insert(intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
    """
    This solution iterates through the intervals and builds a new result list.
    It handles the three possible cases for each interval in relation to the newInterval.

    1.  Initialize an empty `result` list.
    2.  Iterate through each `interval` in the original `intervals` list.
        -   **Case 1: No overlap, current interval is before newInterval.**
            If `interval[end] < newInterval[start]`, there is no overlap and the current
            interval comes first. Add it to the result.
        -   **Case 2: No overlap, current interval is after newInterval.**
            If `interval[start] > newInterval[end]`, there is no overlap and the newInterval
            should come first. Add `newInterval` to the result and then update `newInterval`
            to be the current interval, as we will handle it in the next iteration.
        -   **Case 3: Overlap.**
            If neither of the above is true, the intervals overlap. We merge them by
            updating `newInterval` to be the union of itself and the current interval.
            The start will be the minimum of the two starts, and the end will be the
            maximum of the two ends.
    3.  After the loop, the final `newInterval` (which may have been merged multiple times)
        is added to the result.
    """
    result = []

    for i in range(len(intervals)):
        # Case 2: No overlap, newInterval comes before current interval
        if newInterval[1] < intervals[i][0]:
            result.append(newInterval)
            return result + intervals[i:] # Add the rest of the intervals and return
        # Case 1: No overlap, newInterval comes after current interval
        elif newInterval[0] > intervals[i][1]:
            result.append(intervals[i])
        # Case 3: Overlap exists
        else:
            newInterval = [
                min(newInterval[0], intervals[i][0]),
                max(newInterval[1], intervals[i][1])
            ]

    # Add the final (potentially merged) newInterval
    result.append(newInterval)

    return result
