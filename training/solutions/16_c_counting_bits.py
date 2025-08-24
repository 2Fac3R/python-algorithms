
from typing import List

"""
Solution for: Counting Bits
"""

def countBits(n: int) -> List[int]:
    """
    This solution uses Dynamic Programming with bit manipulation insights.

    Let `dp[i]` be the number of 1's in the binary representation of `i`.

    The key recurrence relation is based on the following observation:
    The number of 1's in `i` is the same as the number of 1's in `i / 2` (`i >> 1`),
    plus an additional 1 if `i` is an odd number.

    - `dp[i] = dp[i >> 1] + (i & 1)`

    Example: i = 5 (101)
    - `i >> 1` is 2 (10). `dp[2]` is 1.
    - `i & 1` is 1 (since 5 is odd).
    - `dp[5] = dp[2] + 1 = 1 + 1 = 2`. This is correct.

    Example: i = 6 (110)
    - `i >> 1` is 3 (11). `dp[3]` is 2.
    - `i & 1` is 0 (since 6 is even).
    - `dp[6] = dp[3] + 0 = 2 + 0 = 2`. This is correct.

    We can build our `dp` array (which we call `ans`) from 0 up to `n` using this relation.
    """
    ans = [0] * (n + 1)
    for i in range(1, n + 1):
        # ans[i] = ans[i // 2] + (i % 2)
        # This is the bit manipulation equivalent:
        ans[i] = ans[i >> 1] + (i & 1)
    return ans
