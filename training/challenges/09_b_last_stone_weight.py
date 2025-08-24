
from typing import List
import heapq

"""
Challenge: Last Stone Weight

You are given an array of integers `stones` where `stones[i]` is the weight of the `i`th stone.

We are playing a game with the stones. On each turn, we choose the **two heaviest** stones and smash them together. Suppose the heaviest stones have weights `x` and `y` with `x <= y`. The result of this smash is:
- If `x == y`, both stones are destroyed.
- If `x != y`, the stone of weight `x` is destroyed, and the stone of weight `y` has new weight `y - x`.

At the end of the game, there is **at most one** stone left. Return the weight of the last remaining stone. If there are no stones left, return 0.

Technique:
This problem requires repeatedly finding the two *heaviest* items. This is a perfect use case for a **Max-Heap**. Since Python's `heapq` is a min-heap, we can simulate a max-heap by storing the negative of the stone weights.
"""

def lastStoneWeight(stones: List[int]) -> int:
    # Your implementation here
    pass

# --- Tests ---
def run_tests():
    test_cases = [
        ([2,7,4,1,8,1], 1),
        ([1], 1),
        ([2,2], 0),
    ]

    for i, (stones, expected) in enumerate(test_cases):
        result = lastStoneWeight(stones)
        if result == expected:
            print(f"Test Case {i + 1}: PASSED")
        else:
            print(f"Test Case {i + 1}: FAILED. Expected {expected}, got {result}")

if __name__ == "__main__":
    run_tests()
