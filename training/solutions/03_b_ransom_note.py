
"""
Solution for: Ransom Note
"""
import collections

def can_construct(ransom_note: str, magazine: str) -> bool:
    """
    This solution uses a hash map (specifically, Python's `collections.Counter`)
    to efficiently count character frequencies.

    1. Create a frequency map (or counter) of all characters in the `magazine`.
       This gives us an inventory of available letters.
    2. Iterate through each character in the `ransom_note`.
    3. For each character needed for the note, check its count in our magazine map.
       - If the count is 0 (or the character isn't in the map), we don't have
         that letter available, so we return `False`.
       - If the count is greater than 0, we "use" one letter by decrementing
         its count in the map.
    4. If we successfully iterate through the entire `ransom_note` without returning
       `False`, it means all characters were available. We can return `True`.
    """
    # collections.Counter is a specialized dictionary for counting hashable objects.
    magazine_counts = collections.Counter(magazine)

    for char in ransom_note:
        if magazine_counts[char] > 0:
            magazine_counts[char] -= 1
        else:
            return False
            
    return True
