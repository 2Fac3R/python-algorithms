
"""
Solution for: Factorial
"""

def factorial(n: int) -> int:
    """
    This function calculates the factorial using recursion.

    - Base Case: If n is 0 or 1, the factorial is 1. This stops the recursion.
    - Recursive Step: If n is greater than 1, the factorial is n multiplied by the
      factorial of (n-1). The function calls itself with a smaller problem.
    """
    # Base Case
    if n <= 1:
        return 1
    # Recursive Step
    else:
        return n * factorial(n - 1)
