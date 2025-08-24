
from typing import List
import heapq

"""
Solution for: Last Stone Weight
"""

def lastStoneWeight(stones: List[int]) -> int:
    """
    This solution uses a max-heap, simulated by storing negative values in a min-heap.

    1. Since we need the heaviest stones, a max-heap is the natural choice. Python's `heapq`
       is a min-heap, so we store the negative of each stone's weight. The "smallest"
       element in this heap will be the largest stone (e.g., -8 is smaller than -2).
    2. We create a list of these negative weights and call `heapq.heapify` to turn it into
       a valid heap in O(n) time.
    3. We loop as long as there is more than one stone (negative weight) in the heap.
    4. In each loop, we pop the two "smallest" elements, which correspond to the two
       largest original stones. Remember to negate them back to get their positive weights.
    5. If the stones have different weights, we calculate the difference, negate it, and
       push it back onto the heap.
    6. After the loop, if the heap is empty, no stones are left, so we return 0. Otherwise,
       we return the weight of the final stone (negating it back to positive).
    """
    # Create a max-heap by storing negative values
    max_heap = [-s for s in stones]
    heapq.heapify(max_heap)

    while len(max_heap) > 1:
        y = -heapq.heappop(max_heap) # First largest
        x = -heapq.heappop(max_heap) # Second largest

        if x != y:
            heapq.heappush(max_heap, -(y - x))
    
    if not max_heap:
        return 0
    else:
        return -max_heap[0]
