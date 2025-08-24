
"""
Solution for: Maximum Sum Subarray of Size K
"""
from typing import List

def max_subarray_sum(arr: List[int], k: int) -> int:
    """
    This solution uses a fixed-size sliding window.
    1. Calculate the sum of the first window of size k. This is our initial max_sum.
    2. Iterate from the k-th element to the end of the array.
    3. In each iteration, "slide" the window by:
       - Adding the current element to the window sum.
       - Subtracting the element that falls out of the window from the left.
    4. Update max_sum if the new window sum is greater.
    """
    if len(arr) < k:
        return 0

    max_sum = 0
    window_sum = 0

    # Calculate sum of the first window
    for i in range(k):
        window_sum += arr[i]
    
    max_sum = window_sum

    # Slide the window from k to the end of the array
    for i in range(k, len(arr)):
        window_sum += arr[i] - arr[i - k]
        max_sum = max(max_sum, window_sum)
        
    return max_sum
