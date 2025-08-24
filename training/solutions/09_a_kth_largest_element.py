
from typing import List
import heapq

"""
Solution for: Kth Largest Element in an Array
"""

def findKthLargest(nums: List[int], k: int) -> int:
    """
    This solution uses a min-heap of a fixed size `k`.

    1. Initialize an empty min-heap.
    2. Iterate through each number in the input array `nums`.
    3. For each number, push it onto our min-heap.
    4. After pushing, if the size of our heap is greater than `k`, it means we have one
       element too many. We pop from the heap, which removes the smallest element.
    5. By consistently removing the smallest element when the heap size exceeds `k`,
       we ensure that the heap always contains the `k` largest elements seen so far.
    6. After the loop, the root of the min-heap (at index 0) is the smallest among the
       `k` largest elements, which is precisely the `k`th largest element overall.

    Time Complexity: O(N log k), where N is the number of elements in nums.
    Space Complexity: O(k) to store the heap.
    """
    min_heap = []
    for num in nums:
        heapq.heappush(min_heap, num)
        if len(min_heap) > k:
            heapq.heappop(min_heap)
    
    return min_heap[0]
