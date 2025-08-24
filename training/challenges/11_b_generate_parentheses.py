
from typing import List

"""
Challenge: Generate Parentheses

Given `n` pairs of parentheses, write a function to generate all combinations of well-formed (valid) parentheses.

Example:
Input: n = 3
Output: ["((()))","(()())","(())()","()(())","()()()"]

Technique:
This is a backtracking problem where the "choices" are to add either an open parenthesis '(' or a close parenthesis ')'. The constraints that guide the backtracking are:
1. You can only add an open parenthesis if you haven't used all `n` of them yet.
2. You can only add a close parenthesis if it wouldn't make the string invalid (i.e., the number of close parentheses is less than the number of open ones).
"""

def generateParenthesis(n: int) -> List[str]:
    # Your implementation here
    pass

# --- Tests ---
def run_tests():
    test_cases = [
        (3, ["((()))","(()())","(())()","()(())","()()()"]),
        (1, ["()"]), 
    ]

    for i, (n, expected) in enumerate(test_cases):
        result = generateParenthesis(n)
        # Sort results for consistent comparison
        sorted_result = sorted(result)
        sorted_expected = sorted(expected)
        if sorted_result == sorted_expected:
            print(f"Test Case {i + 1}: PASSED")
        else:
            print(f"Test Case {i + 1}: FAILED. Expected {sorted_expected}, got {sorted_result}")

if __name__ == "__main__":
    run_tests()
