
from typing import List

"""
Challenge: Counting Bits

Given an integer `n`, return an array `ans` of length `n + 1` such that for each `i` (0 <= i <= n), `ans[i]` is the number of 1's in the binary representation of `i`.

Example:
Input: n = 5
Output: [0,1,1,2,1,2]
Explanation:
0 --> 0
1 --> 1
2 --> 10
3 --> 11
4 --> 100
5 --> 101

Technique:
This problem can be solved with a Dynamic Programming approach that uses bit manipulation. Notice the relationship between the number of bits in `i` and smaller numbers. For example, the number of bits in `i` is related to the number of bits in `i / 2` (`i >> 1`).
"""

def countBits(n: int) -> List[int]:
    # Your implementation here
    pass

# --- Tests ---
def run_tests():
    test_cases = [
        (2, [0,1,1]),
        (5, [0,1,1,2,1,2]),
    ]

    for i, (n, expected) in enumerate(test_cases):
        result = countBits(n)
        if result == expected:
            print(f"Test Case {i + 1}: PASSED")
        else:
            print(f"Test Case {i + 1}: FAILED. Expected {expected}, got {result}")

if __name__ == "__main__":
    run_tests()
