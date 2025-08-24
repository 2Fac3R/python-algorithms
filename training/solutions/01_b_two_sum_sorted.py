
"""
Solution for: Two Sum II - Input Array Is Sorted
"""
from typing import List

def two_sum_sorted(numbers: List[int], target: int) -> List[int]:
    """
    This solution uses the Two Pointers technique on a sorted array.
    - `left` pointer starts at the beginning (index 0).
    - `right` pointer starts at the end.
    - We calculate the sum of the values at the two pointers.
    - If the sum is less than the target, we need a larger sum, so we move the `left` pointer to the right.
    - If the sum is greater than the target, we need a smaller sum, so we move the `right` pointer to the left.
    - If the sum equals the target, we have found our solution. We return the 1-indexed positions.
    """
    left, right = 0, len(numbers) - 1

    while left < right:
        current_sum = numbers[left] + numbers[right]

        if current_sum == target:
            # Return 1-indexed positions
            return [left + 1, right + 1]
        elif current_sum < target:
            left += 1
        else:
            right -= 1
