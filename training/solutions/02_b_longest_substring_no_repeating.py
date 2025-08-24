
"""
Solution for: Longest Substring Without Repeating Characters
"""

def length_of_longest_substring(s: str) -> int:
    """
    This solution uses a variable-size sliding window with a hash map (dictionary)
    to keep track of the last seen index of each character.

    - `start` is the beginning of the window.
    - `max_length` stores the maximum length found so far.
    - `char_map` stores the most recent index of each character.

    We iterate through the string with the `end` pointer.
    If the character at `end` is already in our map and its last seen index is
    within our current window (i.e., `char_map[s[end]] >= start`), we must
    shrink the window by moving `start` to the position right after the last
    occurrence of that character.

    Then, we update the character's last seen index and recalculate the max_length.
    """
    char_map = {}
    max_length = 0
    start = 0

    for end in range(len(s)):
        if s[end] in char_map and char_map[s[end]] >= start:
            start = char_map[s[end]] + 1
        
        char_map[s[end]] = end
        max_length = max(max_length, end - start + 1)
        
    return max_length
