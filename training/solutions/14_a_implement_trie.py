
"""
Solution for: Implement Trie (Prefix Tree)
"""

class TrieNode:
    """Helper class representing each node in the Trie."""
    def __init__(self):
        self.children = {} # Maps a character to a TrieNode
        self.isEndOfWord = False

class Trie:

    def __init__(self):
        """Initializes the trie with a single root node."""
        self.root = TrieNode()

    def insert(self, word: str) -> None:
        """
        Iterates through each character of the word, creating nodes as necessary.
        Marks the final node as the end of a word.
        """
        current = self.root
        for char in word:
            # If the character is not a child of the current node, create a new node.
            if char not in current.children:
                current.children[char] = TrieNode()
            # Move to the child node.
            current = current.children[char]
        current.isEndOfWord = True

    def search(self, word: str) -> bool:
        """
        Traverses the trie. If the full word exists and the final node is marked
        as the end of a word, returns True.
        """
        current = self.root
        for char in word:
            if char not in current.children:
                return False
            current = current.children[char]
        # The word exists only if the path ends at a node marked as the end of a word.
        return current.isEndOfWord

    def startsWith(self, prefix: str) -> bool:
        """
        Traverses the trie. If a path for the prefix exists, returns True.
        """
        current = self.root
        for char in prefix:
            if char not in current.children:
                return False
            current = current.children[char]
        # If we successfully traversed all characters of the prefix, it exists.
        return True
