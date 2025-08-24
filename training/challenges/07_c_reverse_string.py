
"""
Challenge: Reverse String with Recursion

Write a recursive function that takes a string and returns a new string with the characters in reverse order.

Example:
- `reverse_string("hello")` should return `"olleh"`

Technique:
Think about how you can break this problem down. If you have the reversed version of the *rest* of the string, where does the first character go?
"""

def reverse_string(s: str) -> str:
    # Your implementation here
    pass

# --- Tests ---
def run_tests():
    test_cases = [
        ("hello", "olleh"),
        ("Python", "nohtyP"),
        ("a", "a"),
        ("", ""),
    ]

    for i, (s, expected) in enumerate(test_cases):
        result = reverse_string(s)
        if result == expected:
            print(f"Test Case {i + 1}: PASSED")
        else:
            print(f"Test Case {i + 1}: FAILED. Expected {expected}, got {result}")

if __name__ == "__main__":
    run_tests()
