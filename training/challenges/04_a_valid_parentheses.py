
"""
Challenge: Valid Parentheses

Given a string `s` containing just the characters '(', ')', '{', '}', '[' and ']', determine if the input string is valid.

An input string is valid if:
1. Open brackets must be closed by the same type of brackets.
2. Open brackets must be closed in the correct order.
3. Every close bracket has a corresponding open bracket of the same type.

Technique:
This is the quintessential problem for the **Stack** data structure. The LIFO (Last-In, First-Out) nature of a stack is perfect for checking that brackets are closed in the reverse order they were opened.

Instructions:
1. Read the theory on Stacks in `training/techniques/04_stacks_lifo.md`.
2. Implement the `is_valid` function below.
3. Run this file to test your solution.
"""


def is_valid(s: str) -> bool:
    bracket_map = {")": "(", "}": "{", "]": "["}
    stack = []

    for char in s:
        if char in bracket_map.values():  # It's an opening bracket
            stack.append(char)
        elif char in bracket_map.keys():  # It's a closing bracket
            if not stack or bracket_map[char] != stack.pop():
                return False
        else:
            # Character is not a bracket, invalid
            return False

    # The string is valid if and only if the stack is empty at the end
    return not stack


# --- Tests ---
def run_tests():
    test_cases = [
        ("()", True),
        ("()[]{}", True),
        ("(]", False),
        ("([)]", False),
        ("{[]}", True),
        ("", True),
        ("[", False),
    ]

    for i, (s, expected) in enumerate(test_cases):
        result = is_valid(s)
        if result == expected:
            print(f"Test Case {i + 1}: PASSED")
        else:
            print(
                f"Test Case {i + 1}: FAILED. Expected {expected}, got {result}")


if __name__ == "__main__":
    run_tests()
