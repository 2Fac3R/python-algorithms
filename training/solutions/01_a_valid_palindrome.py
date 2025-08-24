
"""
Solution for: Valid Palindrome
"""

def is_palindrome(s: str) -> bool:
    """
    This solution uses the Two Pointers technique.
    - `left` pointer starts at the beginning.
    - `right` pointer starts at the end.
    - The pointers move towards each other.
    - In each step, we skip non-alphanumeric characters.
    - We compare the characters at the `left` and `right` pointers (in lowercase).
    - If they are ever not equal, we know it's not a palindrome.
    - If the pointers meet or cross, it means all characters have been checked successfully.
    """
    left, right = 0, len(s) - 1

    while left < right:
        # Move the left pointer until it points to an alphanumeric character
        while left < right and not s[left].isalnum():
            left += 1
        
        # Move the right pointer until it points to an alphanumeric character
        while left < right and not s[right].isalnum():
            right -= 1

        # Compare the two characters (case-insensitive)
        if s[left].lower() != s[right].lower():
            return False

        # Move pointers inward
        left += 1
        right -= 1

    return True
