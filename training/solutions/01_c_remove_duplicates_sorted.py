
"""
Solution for: Remove Duplicates from Sorted Array
"""
from typing import List

def remove_duplicates(nums: List[int]) -> int:
    """
    This solution uses the Fast & Slow pointer technique.

    - `slow` (or `insert_index`): This pointer stays at the last confirmed position of a unique element.
    - `fast`: This pointer iterates through the entire array to find the next unique element.

    1. If the list is empty, there are 0 unique elements.
    2. Initialize `slow` to 0.
    3. The `fast` pointer starts at index 1 and moves to the end.
    4. In each iteration, we compare `nums[fast]` with `nums[slow]`.
       - If they are the same, it's a duplicate. We do nothing but advance `fast`.
       - If they are different, it means `nums[fast]` is a new unique element. We then:
         a. Move the `slow` pointer one step forward.
         b. Copy the value from `nums[fast]` to `nums[slow]`.
    5. After the loop, the number of unique elements is `slow + 1`.
    """
    if not nums:
        return 0

    slow = 0
    for fast in range(1, len(nums)):
        if nums[fast] != nums[slow]:
            slow += 1
            nums[slow] = nums[fast]
    
    return slow + 1
