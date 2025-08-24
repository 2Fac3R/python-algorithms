
"""
Challenge: Ransom Note

Given two strings, `ransom_note` and `magazine`, return `true` if `ransom_note` can be constructed by using the letters from `magazine` and `false` otherwise.

Each letter in `magazine` can only be used once in `ransom_note`.
"""
from collections import Counter


def can_construct(ransom_note: str, magazine: str) -> bool:
    magazine_counts = Counter(magazine)

    for char in ransom_note:
        if magazine_counts[char] > 0:
            magazine_counts[char] -= 1
        else:
            return False

    return True


# --- Tests ---
def run_tests():
    test_cases = [
        ("a", "b", False),
        ("aa", "ab", False),
        ("aa", "aab", True),
        ("fihij", "ihjijf", True),
        ("apple", "paleppa", True)
    ]

    for i, (note, mag, expected) in enumerate(test_cases):
        result = can_construct(note, mag)
        if result == expected:
            print(f"Test Case {i + 1}: PASSED")
        else:
            print(
                f"Test Case {i + 1}: FAILED. Expected {expected}, got {result}")


if __name__ == "__main__":
    run_tests()
