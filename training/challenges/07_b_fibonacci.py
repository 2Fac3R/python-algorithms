
"""
Challenge: Fibonacci Number

The Fibonacci numbers, commonly denoted `F(n)`, form a sequence such that each number is the sum of the two preceding ones, starting from 0 and 1.

F(0) = 0, F(1) = 1
F(n) = F(n - 1) + F(n - 2), for n > 1.

Given `n`, calculate `F(n)` using recursion.

This problem is a classic example of tree-like recursion, where a single call can result in multiple subsequent calls.
"""

def fib(n: int) -> int:
    # Your implementation here
    pass

# --- Tests ---
def run_tests():
    test_cases = [
        (0, 0),
        (1, 1),
        (2, 1),
        (3, 2),
        (4, 3),
        (5, 5),
        (10, 55),
    ]

    for i, (n, expected) in enumerate(test_cases):
        result = fib(n)
        if result == expected:
            print(f"Test Case {i + 1}: PASSED")
        else:
            print(f"Test Case {i + 1}: FAILED. Expected {expected}, got {result}")

if __name__ == "__main__":
    run_tests()
