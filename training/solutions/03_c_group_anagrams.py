
"""
Solution for: Group Anagrams
"""
from typing import List
import collections

def group_anagrams(strs: List[str]) -> List[List[str]]:
    """
    This solution uses a hash map to group anagrams.

    The core idea is that all anagrams, when their letters are sorted, will result
    in the exact same string. This sorted string can be used as a key in our hash map.

    1. Initialize a dictionary, `anagram_map`, where keys will be the sorted-string
       representation and values will be lists of the original strings.
    2. Iterate through each string in the input list `strs`.
    3. For each string, create its canonical key by sorting it.
       - e.g., "eat" -> "aet", "tea" -> "aet"
    4. Use this key to append the original string to the corresponding list in the
       `anagram_map`.
    5. After iterating through all strings, the values of the `anagram_map` will be
       the lists of grouped anagrams.
    """
    anagram_map = collections.defaultdict(list)

    for s in strs:
        # Create a key by sorting the string. A tuple is used because it's hashable.
        key = tuple(sorted(s))
        anagram_map[key].append(s)
    
    return list(anagram_map.values())
