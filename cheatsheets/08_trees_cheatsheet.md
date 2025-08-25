
# Cheatsheet: Trees

**Core Concept:** A non-linear data structure of nodes connected in a parent-child relationship. Essential for representing hierarchies.

---

### `TreeNode` Class

```python
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
```

---

### Binary Tree (BT) vs. Binary Search Tree (BST)

| Type | Property |
|:---|:---|
| **Binary Tree** | Each node has **at most 2** children (`left`, `right`). |
| **Binary Search Tree**| A BT where for every node: `left_child.val < node.val < right_child.val`. |

---

### Tree Traversal Algorithms

| Approach | Traversal | Order | Data Structure | Key Use Case |
|:---|:---|:---|:---|:---|
| **DFS** | Pre-order | Root -> Left -> Right | Stack (Recursion) | Copying a tree. |
| **DFS** | In-order | Left -> Root -> Right | Stack (Recursion) | Getting values from a **BST in sorted order**. |
| **DFS** | Post-order | Left -> Right -> Root | Stack (Recursion) | Deleting nodes. |
| **BFS** | Level-order | Visit layer by layer | Queue (`deque`) | Finding the shortest path from root to a node. |

---

### Implementation Snippets

**DFS In-order Traversal:**
```python
def inorder_traversal(node):
    if not node:
        return
    inorder_traversal(node.left)
    print(node.val) # Process node
    inorder_traversal(node.right)
```

**BFS Level-order Traversal:**
```python
from collections import deque

def level_order_traversal(root):
    if not root: return
    queue = deque([root])
    while queue:
        node = queue.popleft()
        print(node.val) # Process node
        if node.left: queue.append(node.left)
        if node.right: queue.append(node.right)
```
