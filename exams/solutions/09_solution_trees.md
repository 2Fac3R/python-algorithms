
# Solutions: Exam - Trees

---

### Question 1 (Concept)

What is the key property that distinguishes a Binary Search Tree (BST) from a regular Binary Tree (BT)?

- **Answer:** For any given node in a BST, all values in its left subtree must be **less than** the node's value, and all values in its right subtree must be **greater than** the node's value.

---

### Question 2 (Traversal)

Which Depth-First Search (DFS) traversal method, when applied to a valid Binary Search Tree, will visit the nodes in ascending sorted order?

- **Correct Answer:** b) In-order
- **Explanation:** The In-order traversal pattern is `Left -> Root -> Right`, which naturally follows the ordering property of a BST.

---

### Question 3 (Data Structures)

To implement a Breadth-First Search (BFS) or Level-Order Traversal, what auxiliary data structure is typically used?

- **Answer:** A Queue (in Python, `collections.deque`).

---

### Question 4 (Analysis)

Consider the following simple tree:
`root = Node(10, left=Node(5), right=Node(15))`

What would be the sequence of values visited in a **Pre-order** traversal?

- **Answer:** `[10, 5, 15]`
- **Explanation:** Pre-order traversal follows the pattern `Root -> Left -> Right`.

