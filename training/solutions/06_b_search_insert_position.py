
"""
Solution for: Search Insert Position
"""
from typing import List

def search_insert(nums: List[int], target: int) -> int:
    """
    This solution is a modification of the standard Binary Search algorithm.

    The search process is the same: we adjust `left` and `right` pointers to
    narrow down the search space.

    - If we find the `target`, we return its index `mid` immediately.

    The key difference is what happens when the loop terminates (when `left > right`).
    At this point, the `left` pointer indicates the first position in the array
    that is greater than or equal to the target. This is precisely the index
    where the target would be inserted to maintain the sorted order.

    Consider the final state:
    - All elements to the left of `left` are smaller than the target.
    - All elements to the right of `right` (and `left`) are greater than the target.
    - Therefore, `left` is the correct insertion point.
    """
    left, right = 0, len(nums) - 1

    while left <= right:
        mid = left + (right - left) // 2

        if nums[mid] == target:
            return mid
        elif nums[mid] < target:
            left = mid + 1
        else:
            right = mid - 1

    # If the loop finishes, `left` is the insertion point.
    return left
