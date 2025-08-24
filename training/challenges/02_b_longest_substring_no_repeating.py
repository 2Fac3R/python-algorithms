
"""
Challenge: Longest Substring Without Repeating Characters

Given a string `s`, find the length of the longest substring without repeating characters.

Technique:
This problem can be efficiently solved using a **Variable-Size Sliding Window**. You expand the window by moving the `end` pointer and shrink it by moving the `start` pointer whenever a duplicate character is found. A hash map (dictionary) is useful for keeping track of characters currently in the window.

Instructions:
1. Read the theory on Sliding Window in `training/techniques/02_sliding_window.md`.
2. Implement the `length_of_longest_substring` function below.
3. Run this file to test your solution.
"""


def length_of_longest_substring(s: str) -> int:
    # Your implementation here
    pass

# --- Tests ---


def run_tests():
    test_cases = [
        ("abcabcbb", 3),  # "abc"
        ("bbbbb", 1),     # "b"
        ("pwwkew", 3),    # "wke"
        ("", 0),
        ("dvdf", 3),      # "vdf"
    ]

    for i, (s, expected) in enumerate(test_cases):
        result = length_of_longest_substring(s)
        if result == expected:
            print(f"Test Case {i + 1}: PASSED")
        else:
            print(
                f"Test Case {i + 1}: FAILED. Expected {expected}, got {result}")


if __name__ == "__main__":
    run_tests()
