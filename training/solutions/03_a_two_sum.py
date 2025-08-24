
"""
Solution for: Two Sum
"""
from typing import List

def two_sum(nums: List[int], target: int) -> List[int]:
    """
    This solution uses a hash map (dictionary) to store the numbers we've seen
    and their indices.

    We iterate through the list of numbers. For each number, we calculate its
    "complement" (the other number that would add up to the target).

    - complement = target - current_number

    We then check if this complement is already in our hash map.
    - If it is, we have found our pair. We can return the index of the complement
      (stored in the map) and the index of the current number.
    - If it's not, we add the current number and its index to the map so we can
      find it in a future iteration.

    This approach has a time complexity of O(n) because we iterate through the list
    once, and each hash map lookup is O(1) on average.
    """
    num_map = {}
    for i, num in enumerate(nums):
        complement = target - num
        if complement in num_map:
            return [num_map[complement], i]
        num_map[num] = i
