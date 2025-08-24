
"""
Challenge: Valid Palindrome

A phrase is a palindrome if, after converting all uppercase letters into lowercase letters
and removing all non-alphanumeric characters, it reads the same forward and backward.
Alphanumeric characters include letters and numbers.

Given a string s, return true if it is a palindrome, or false otherwise.

Technique: 
This problem is a classic use case for the **Two Pointers** technique with pointers
starting at opposite ends of the string.

Instructions:
1. Read the theory on Two Pointers in `training/techniques/01_two_pointers.md`.
2. Implement the `is_palindrome` function below.
3. Run this file using `python training/challenges/01_a_valid_palindrome.py` to test your solution.
"""


def is_palindrome(s: str) -> bool:
    s = ''.join(char for char in s.lower() if char.isalnum())

    left, right = 0, len(s) - 1

    while left < right:
        if s[left] == s[right]:
            left += 1
            right -= 1
        else:
            return False
    return True


# --- Tests ---
def run_tests():
    test_cases = [
        ("A man, a plan, a canal: Panama", True),
        ("race a car", False),
        (" ", True),
        ("level", True),
        ("Was it a car or a cat I saw?", True),
        ("not a palindrome", False),
    ]

    for i, (s, expected) in enumerate(test_cases):
        result = is_palindrome(s)
        if result == expected:
            print(f"Test Case {i + 1}: PASSED")
        else:
            print(
                f"Test Case {i + 1}: FAILED. Expected {expected}, got {result}")


if __name__ == "__main__":
    run_tests()
