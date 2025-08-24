
from typing import List, Dict, Set

"""
Solution for: Word Search II
"""

class TrieNode:
    def __init__(self):
        self.children: Dict[str, TrieNode] = {}
        self.isEndOfWord = False

class Solution:
    def findWords(self, board: List[List[str]], words: List[str]) -> List[str]:
        """
        This solution combines a Trie with a backtracking (DFS) search.

        1.  **Build the Trie:** Insert all words from the `words` list into a Trie.
            This allows for efficient prefix searching.
        2.  **Iterate and Search:** Iterate through every cell on the board. For each cell,
            start a DFS search if the character exists at the root of the Trie.
        3.  **DFS/Backtracking Logic:**
            - The `dfs` function explores neighbors (up, down, left, right).
            - It takes the current board position (r, c), the current Trie node, and the
              word being built so far.
            - **Pruning:** The search is pruned immediately if the current character on the
              board does not correspond to a child of the current Trie node.
            - **Marking:** To avoid reusing cells, we mark the current cell as visited
              (e.g., by changing it to '#') before exploring its neighbors.
            - **Finding a Word:** If we reach a Trie node where `isEndOfWord` is True, we add
              the current word to our result set. We then set `isEndOfWord` to False
              to avoid adding the same word multiple times.
            - **Backtrack:** After exploring from a cell, we restore its original character
              so it can be used in other paths.
        """
        root = TrieNode()
        for word in words:
            node = root
            for char in word:
                if char not in node.children:
                    node.children[char] = TrieNode()
                node = node.children[char]
            node.isEndOfWord = True

        rows, cols = len(board), len(board[0])
        result: Set[str] = set()
        visited: Set[tuple[int, int]] = set()

        def dfs(r, c, node, word):
            if (
                r < 0 or c < 0 or
                r >= rows or c >= cols or
                (r, c) in visited or
                board[r][c] not in node.children
            ):
                return

            visited.add((r, c))
            node = node.children[board[r][c]]
            word += board[r][c]

            if node.isEndOfWord:
                result.add(word)
                node.isEndOfWord = False # Avoid duplicates

            dfs(r + 1, c, node, word)
            dfs(r - 1, c, node, word)
            dfs(r, c + 1, node, word)
            dfs(r, c - 1, node, word)

            visited.remove((r, c)) # Backtrack

        for r in range(rows):
            for c in range(cols):
                dfs(r, c, root, "")
        
        return list(result)
