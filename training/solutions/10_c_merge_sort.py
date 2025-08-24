
from typing import List

"""
Solution for: Implement Merge Sort
"""

def merge_sort(nums: List[int]) -> List[int]:
    """
    This function implements the Merge Sort algorithm, a classic Divide and Conquer strategy.
    """
    # 1. Divide: Find the middle of the array and split it into two halves.
    # Base Case: If the array has 0 or 1 elements, it is already sorted.
    if len(nums) <= 1:
        return nums

    mid = len(nums) // 2
    left_half = nums[:mid]
    right_half = nums[mid:]

    # 2. Conquer: Recursively sort both halves.
    sorted_left = merge_sort(left_half)
    sorted_right = merge_sort(right_half)

    # 3. Combine: Merge the two sorted halves.
    return merge(sorted_left, sorted_right)

def merge(left: List[int], right: List[int]) -> List[int]:
    """
    Helper function to merge two sorted arrays into one sorted array.
    """
    merged = []
    left_idx, right_idx = 0, 0

    # Loop while there are elements in both lists
    while left_idx < len(left) and right_idx < len(right):
        if left[left_idx] < right[right_idx]:
            merged.append(left[left_idx])
            left_idx += 1
        else:
            merged.append(right[right_idx])
            right_idx += 1

    # Append any remaining elements from the left or right half
    merged.extend(left[left_idx:])
    merged.extend(right[right_idx:])
    
    return merged
