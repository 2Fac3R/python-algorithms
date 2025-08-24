
"""
Challenge: Climbing Stairs

You are climbing a staircase. It takes `n` steps to reach the top.

Each time you can either climb 1 or 2 steps. In how many distinct ways can you climb to the top?

Example:
Input: n = 3
Output: 3
Explanation: There are three ways to climb to the top.
1. 1 step + 1 step + 1 step
2. 1 step + 2 steps
3. 2 steps + 1 step

Technique:
This is a classic introductory **Dynamic Programming** problem. Notice that to reach step `n`, you must have come from either step `n-1` or step `n-2`. Therefore, the total number of ways to reach step `n` is `ways(n-1) + ways(n-2)`. This is the Fibonacci sequence!
"""

def climbStairs(n: int) -> int:
    # Your implementation here
    pass

# --- Tests ---
def run_tests():
    test_cases = [
        (2, 2),
        (3, 3),
        (4, 5),
        (5, 8),
    ]

    for i, (n, expected) in enumerate(test_cases):
        result = climbStairs(n)
        if result == expected:
            print(f"Test Case {i + 1}: PASSED")
        else:
            print(f"Test Case {i + 1}: FAILED. Expected {expected}, got {result}")

if __name__ == "__main__":
    run_tests()
