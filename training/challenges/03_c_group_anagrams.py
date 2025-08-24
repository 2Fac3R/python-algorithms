
"""
Challenge: Group Anagrams

Given an array of strings `strs`, group the anagrams together. You can return the answer in any order.

An Anagram is a word or phrase formed by rearranging the letters of a different word or phrase, typically using all the original letters exactly once.

Technique:
The key to this problem is finding a way to identify anagrams. A **Hash Table** is the perfect tool. The trick is to create a canonical (standard) representation for each word to use as a key. All words that are anagrams of each other will map to the same key. A sorted version of the string is a great choice for this key.

Instructions:
1. Read the theory on Hash Tables in `training/techniques/03_hash_map_patterns.md`.
2. Implement the `group_anagrams` function below.
3. Run this file to test your solution.
"""
from typing import List

def group_anagrams(strs: List[str]) -> List[List[str]]:
    # Your implementation here
    pass

# --- Tests ---
def run_tests():
    test_cases = [
        (["eat","tea","tan","ate","nat","bat"], [["bat"],["nat","tan"],["ate","eat","tea"]]),
        ([""], [[""]]),
        (["a"], [["a"]]),
    ]

    for i, (strs, expected) in enumerate(test_cases):
        result = group_anagrams(strs)
        # Sort the inner and outer lists for consistent comparison
        sorted_result = sorted([sorted(group) for group in result])
        sorted_expected = sorted([sorted(group) for group in expected])
        
        if sorted_result == sorted_expected:
            print(f"Test Case {i + 1}: PASSED")
        else:
            print(f"Test Case {i + 1}: FAILED. Expected {sorted_expected}, got {sorted_result}")

if __name__ == "__main__":
    run_tests()
