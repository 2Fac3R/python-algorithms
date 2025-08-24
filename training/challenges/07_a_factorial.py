
"""
Challenge: Factorial

Write a recursive function that calculates the factorial of a non-negative integer `n`.
The factorial of `n`, denoted as `n!`, is the product of all positive integers up to `n`.
`n! = n * (n-1) * (n-2) * ... * 1`

By definition, `0! = 1`.

This is the classic introductory problem for recursion.

Instructions:
1. Identify the base case (the simplest version of the problem).
2. Identify the recursive step (how to break the problem down into a smaller version of itself).
3. Implement the `factorial` function below.
"""

def factorial(n: int) -> int:
    # Your implementation here
    pass

# --- Tests ---
def run_tests():
    test_cases = [
        (0, 1),
        (1, 1),
        (5, 120), # 5 * 4 * 3 * 2 * 1
        (10, 3628800),
    ]

    for i, (n, expected) in enumerate(test_cases):
        result = factorial(n)
        if result == expected:
            print(f"Test Case {i + 1}: PASSED")
        else:
            print(f"Test Case {i + 1}: FAILED. Expected {expected}, got {result}")

if __name__ == "__main__":
    run_tests()
