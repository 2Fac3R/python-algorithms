
# Data Structure: Tries (Prefix Trees)

A **Trie** (pronounced "try", from "retrieval") is a specialized tree-like data structure used for storing and retrieving strings efficiently. Unlike other trees, a Trie is not a binary tree. Instead, each node can have multiple children, typically one for each possible character in the alphabet.

Each node in a Trie represents a single character. A path from the root to a node represents a **prefix**. A special marker on a node indicates the end of a complete word.

### Structure of a `TrieNode`

The building block of a Trie is the `TrieNode`. Each node contains two key pieces of information:

1.  **`children`**: A hash map (dictionary) where keys are characters and values are pointers to other `TrieNode` objects. For example, `{'a': TrieNode(), 'b': TrieNode()}`.
2.  **`isEndOfWord`**: A boolean flag that is `True` if the node represents the end of a complete word, and `False` otherwise.

```python
class TrieNode:
    def __init__(self):
        self.children = {}
        self.isEndOfWord = False
```

---

## Core Operations

Let `L` be the length of the word or prefix.

### 1. `insert(word)` - O(L)

To insert a word, you traverse the Trie from the root, character by character.

1.  Start at the `root` node.
2.  For each character in the word, check if it exists in the current node's `children` dictionary.
3.  If it doesn't exist, create a new `TrieNode` and add it to the `children`.
4.  Move to that child node.
5.  After iterating through all characters, mark the final node's `isEndOfWord` flag as `True`.

### 2. `search(word)` - O(L)

To search for a complete word, you traverse the Trie.

1.  Start at the `root`.
2.  For each character, move to the corresponding child node.
3.  If at any point a character is not in the current node's `children`, the word does not exist, so return `False`.
4.  After iterating through all characters, you must check if the final node's `isEndOfWord` flag is `True`. If it is, the word exists. If it's `False`, it means you only found a prefix, not a complete word.

### 3. `startsWith(prefix)` - O(L)

This is similar to `search`, but simpler.

1.  Traverse the Trie according to the characters in the `prefix`.
2.  If you can successfully traverse the entire prefix (i.e., you never hit a missing character), return `True`.
3.  You do **not** need to check the `isEndOfWord` flag.

### Common Use Cases

-   **Autocomplete Systems:** Suggesting words as a user types.
-   **Spell Checkers:** Quickly verifying if a word is in a dictionary.
-   **IP Routing:** Routers use a similar structure to find the longest matching prefix for an IP address.
