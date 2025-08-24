
# Data Structure: Trees

Trees are a fundamental non-linear data structure that consists of nodes in a parent-child relationship. They are extremely common in computer science for representing hierarchical data.

### Core Terminology

- **Node:** The basic unit of a tree, containing a value and pointers to its children.
- **Root:** The topmost node in a tree.
- **Edge:** The link between two nodes.
- **Parent:** A node that has child nodes.
- **Child:** A node that has a parent node.
- **Leaf:** A node with no children.
- **Height:** The length of the longest path from a node to a leaf.
- **Depth:** The length of the path from the root to a node.

### Binary Tree (BT)

A binary tree is a tree in which each node has **at most two children**, referred to as the `left` child and the `right` child.

### Binary Search Tree (BST)

A Binary Search Tree is a special type of Binary Tree with a specific ordering property that makes searching very efficient (O(log n) on average).

For any given node:
1.  All values in its **left subtree** are **less than** the node's value.
2.  All values in its **right subtree** are **greater than** the node's value.
3.  Both the left and right subtrees must also be binary search trees.

### Python Node Implementation

All tree problems use a `TreeNode` class like this:

```python
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
```

---

## Tree Traversal Algorithms

Traversal is the process of visiting (checking or updating) each node in a tree. There are two main approaches:

### 1. Depth-First Search (DFS)

DFS explores as far as possible down one branch before backtracking. It is naturally implemented using **recursion** (which uses the call stack implicitly).

There are three main types of DFS traversal:

- **Pre-order:** `Root -> Left -> Right`
- **In-order:** `Left -> Root -> Right` (For a BST, this traversal visits nodes in sorted order!)
- **Post-order:** `Left -> Right -> Root`

### 2. Breadth-First Search (BFS)

BFS explores the tree layer by layer. It visits all the nodes at a given depth before moving to the next level. It is implemented using a **Queue**.
