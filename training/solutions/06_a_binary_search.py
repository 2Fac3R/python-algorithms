
"""
Solution for: Binary Search
"""
from typing import List

def search(nums: List[int], target: int) -> int:
    """
    This is the classic iterative implementation of Binary Search.

    1. Initialize `left` and `right` pointers to the start (0) and end
       (len(nums) - 1) of the array.
    2. Loop as long as `left <= right`. This condition ensures we cover the
       entire search space, including the case of a single element.
    3. Calculate the `mid` point. `mid = left + (right - left) // 2` is a robust
       way to do this, preventing potential overflow in other languages.
    4. Compare the middle element `nums[mid]` with the `target`:
       - If `nums[mid] == target`, we found it. Return `mid`.
       - If `nums[mid] < target`, the target must be in the right half, so we
         discard the left half by setting `left = mid + 1`.
       - If `nums[mid] > target`, the target must be in the left half, so we
         discard the right half by setting `right = mid - 1`.
    5. If the loop terminates, `left` has crossed `right`, which means the
       target was not found. Return -1.
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

    return -1
