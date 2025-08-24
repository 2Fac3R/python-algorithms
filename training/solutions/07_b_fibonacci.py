
"""
Solution for: Fibonacci Number
"""

def fib(n: int) -> int:
    """
    This function calculates the n-th Fibonacci number using recursion.

    - Base Cases: 
        - If n is 0, the result is 0.
        - If n is 1, the result is 1.
    - Recursive Step: If n > 1, the result is the sum of the previous two
      Fibonacci numbers, fib(n-1) and fib(n-2).

    Note: This purely recursive solution is very inefficient (O(2^n)) because it
    recalculates the same values many times. It serves as a classic example of
    a problem that can be greatly optimized with dynamic programming (memoization).
    """
    # Base Cases
    if n == 0:
        return 0
    if n == 1:
        return 1
    
    # Recursive Step
    return fib(n - 1) + fib(n - 2)
