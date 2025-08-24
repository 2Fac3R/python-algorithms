
from typing import List

"""
Challenge: Word Search II

Given an `m x n` `board` of characters and a list of strings `words`, return all words on the board.

Each word must be constructed from letters of sequentially adjacent cells, where adjacent cells are horizontally or vertically neighboring. The same letter cell may not be used more than once in a word.

Example:
Input: board = [["o","a","a","n"],["e","t","a","e"],["i","h","k","r"],["i","f","l","v"]], words = ["oath","pea","eat","rain"]
Output: ["eat","oath"]

Technique:
A brute-force approach where you search for each word individually is too slow. The optimal solution uses a **Trie** to store all the words from the dictionary. Then, you perform a single **backtracking (DFS)** search from each cell on the board. As you traverse the board, you also traverse the Trie. This allows you to search for all words simultaneously and prune search paths that don't match any prefix in the dictionary.
"""

class Solution:
    def findWords(self, board: List[List[str]], words: List[str]) -> List[str]:
        # Your implementation here
        pass

# --- Tests ---
def run_tests():
    solver = Solution()
    test_cases = [
        (
            [["o","a","a","n"],["e","t","a","e"],["i","h","k","r"],["i","f","l","v"]],
            ["oath","pea","eat","rain"],
            ["oath", "eat"]
        ),
        (
            [["a","b"],["c","d"]],
            ["abcb"],
            []
        )
    ]

    for i, (board, words, expected) in enumerate(test_cases):
        result = solver.findWords(board, words)
        # Sort for consistent comparison
        if sorted(result) == sorted(expected):
            print(f"Test Case {i + 1}: PASSED")
        else:
            print(f"Test Case {i + 1}: FAILED. Expected {sorted(expected)}, got {sorted(result)}")

if __name__ == "__main__":
    run_tests()
