
"""
Solution for: Climbing Stairs
"""

def climbStairs(n: int) -> int:
    """
    This solution uses Dynamic Programming with a bottom-up (Tabulation) approach.
    The problem follows the pattern of the Fibonacci sequence.

    Let `dp[i]` be the number of ways to reach step `i`.
    - `dp[0]` = 1 (1 way to be at the start)
    - `dp[1]` = 1 (1 way to take 1 step)
    - `dp[2]` = `dp[1]` + `dp[0]` = 2
    - `dp[i]` = `dp[i-1]` + `dp[i-2]`

    We can optimize the space from O(n) to O(1) by only keeping track of the
    last two values, since we only need `n-1` and `n-2` to calculate `n`.
    """
    if n <= 1:
        return 1

    # O(1) space solution
    one_step_back = 1
    two_steps_back = 1

    for _ in range(2, n + 1):
        current_ways = one_step_back + two_steps_back
        two_steps_back = one_step_back
        one_step_back = current_ways
    
    return one_step_back
