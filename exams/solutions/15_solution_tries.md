
# Solutions: Exam - Tries (Prefix Trees)

---

### Question 1 (Concept)

What is the primary advantage of using a Trie over a hash set for storing a dictionary of words?

- **Correct Answer:** c) It is very efficient for `startsWith` (prefix) searches.
- **Explanation:** While a hash set has O(L) search time for a full word, it cannot efficiently find all words with a given prefix. A Trie is designed for this specific task.

---

### Question 2 (Structure)

What are the two essential attributes of a `TrieNode` class?

1.  A `children` collection (usually a dictionary/hash map) to point to child nodes.
2.  An `isEndOfWord` boolean flag to mark if the node represents the end of a complete word.

---

### Question 3 (Analysis)

You have a Trie and you call `search("app")`. The function traverses the nodes for 'a', 'p', and 'p' successfully. However, it returns `False`. What is the most likely reason for this?

- **Reason:** The `isEndOfWord` flag on the final node (for the last 'p') is `False`. This means that while "app" exists as a prefix (e.g., from the word "apple"), it was never inserted as a complete word itself.

---

### Question 4 (Complexity)

What is the time complexity of inserting a word of length `L` into a Trie?

- **Answer:** O(L)
- **Explanation:** The algorithm iterates through the length of the word once, performing a constant number of operations at each character.

