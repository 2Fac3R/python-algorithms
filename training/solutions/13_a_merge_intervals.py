
from typing import List

"""
Solution for: Merge Intervals
"""

def merge(intervals: List[List[int]]) -> List[List[int]]:
    """
    This solution follows the standard Merge Intervals pattern.

    1.  **Sort:** Sort the intervals based on their start time. This is the most critical step.
    2.  **Initialize:** Create a `merged` list and initialize it with the first interval from
        the sorted list.
    3.  **Iterate and Merge:** Loop through the remaining intervals.
        - Get the last interval from our `merged` list.
        - If the current interval's start is less than or equal to the last merged
          interval's end, they overlap.
        - If they overlap, update the end of the last merged interval to be the maximum
          of the two end times.
        - If they don't overlap, simply append the current interval to the `merged` list.
    4.  Return the `merged` list.
    """
    if not intervals:
        return []

    # 1. Sort the intervals by their start time.
    intervals.sort(key=lambda i: i[0])

    # 2. Initialize merged list
    merged = [intervals[0]]

    # 3. Iterate and Merge
    for current_interval in intervals[1:]:
        last_merged = merged[-1]

        # Check for overlap
        if current_interval[0] <= last_merged[1]:
            # Merge by updating the end of the last interval in the merged list
            last_merged[1] = max(last_merged[1], current_interval[1])
        else:
            # No overlap, add the new interval
            merged.append(current_interval)
            
    return merged
