
# Cheatsheet: Tries (Prefix Trees)

**Core Concept:** A special tree for storing and searching strings. Each node is a character, and each path from the root is a prefix. Extremely fast for prefix-based operations.

**Time Complexity:** All core operations (`insert`, `search`, `startsWith`) are **O(L)**, where `L` is the length of the word/prefix. This is much faster than checking against a list of strings.

---

### `TrieNode` Structure

The essential building block.

```python
class TrieNode:
    def __init__(self):
        self.children = {}      # dict of char -> TrieNode
        self.isEndOfWord = False
```

---

### Core Logic

| Operation | Logic | Key Check |
|:---|:---|:---|
| **`insert(word)`** | Traverse, create nodes if they don't exist. | Mark the last node: `node.isEndOfWord = True`. |
| **`search(word)`** | Traverse all characters in the word. | Must find the full path **AND** the last node must have `isEndOfWord == True`. |
| **`startsWith(prefix)`**| Traverse all characters in the prefix. | Only needs to find the full path. `isEndOfWord` doesn't matter. |

---

### Common Use Cases

-   **Autocomplete / Typeahead:** Suggesting words as a user types.
-   **Spell Checkers & Dictionaries:** Quickly verifying if a word is valid.
-   **IP Routing Tables:** Finding the longest matching prefix.
