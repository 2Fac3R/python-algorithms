
"""
Challenge: Implement Trie (Prefix Tree)

A Trie (pronounced "try") or prefix tree is a tree data structure used to efficiently store and retrieve keys in a dataset of strings. There are various applications of this data structure, such as autocomplete and spellchecker.

Implement the Trie class:
- `__init__()` Initializes the trie object.
- `insert(word: str)` Inserts the string `word` into the trie.
- `search(word: str)` Returns `True` if the string `word` is in the trie (i.e., was inserted before), and `False` otherwise.
- `startsWith(prefix: str)` Returns `True` if there is a previously inserted string `word` that has the `prefix`, and `False` otherwise.

Technique:
This challenge requires you to build the Trie data structure from scratch. You will need a helper `TrieNode` class to represent each node. The main `Trie` class will have a `root` node and will orchestrate the operations.
"""

class TrieNode:
    # Helper class for the node structure
    def __init__(self):
        self.children = {}
        self.isEndOfWord = False

class Trie:

    def __init__(self):
        # Your implementation here
        pass

    def insert(self, word: str) -> None:
        # Your implementation here
        pass

    def search(self, word: str) -> bool:
        # Your implementation here
        pass

    def startsWith(self, prefix: str) -> bool:
        # Your implementation here
        pass

# --- Tests ---
def run_tests():
    trie = Trie()
    trie.insert("apple")
    print(f"Test 1 (search 'apple'): {'PASSED' if trie.search('apple') else 'FAILED'}")
    print(f"Test 2 (search 'app'): {'PASSED' if not trie.search('app') else 'FAILED'}")
    print(f"Test 3 (startsWith 'app'): {'PASSED' if trie.startsWith('app') else 'FAILED'}")
    trie.insert("app")
    print(f"Test 4 (search 'app'): {'PASSED' if trie.search('app') else 'FAILED'}")

if __name__ == "__main__":
    run_tests()
