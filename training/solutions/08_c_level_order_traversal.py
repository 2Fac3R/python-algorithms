
from typing import Optional, List
import collections

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

"""
Solution for: Binary Tree Level Order Traversal
"""

def levelOrder(root: Optional[TreeNode]) -> List[List[int]]:
    """
    This solution uses Breadth-First Search (BFS) with a queue.

    1. Initialize an empty list `result` to store the levels.
    2. If the root is None, return the empty list.
    3. Initialize a queue (`collections.deque`) and add the root node.
    4. Loop while the queue is not empty:
       a. Get the number of nodes currently in the queue. This is the size of the current level.
       b. Create a new list `current_level` to store the values of this level's nodes.
       c. Loop `level_size` times:
          i. Dequeue a node.
          ii. Add its value to `current_level`.
          iii. If the node has a left child, enqueue it.
          iv. If the node has a right child, enqueue it.
       d. Append `current_level` to the main `result` list.
    5. Return `result`.
    """
    result = []
    if not root:
        return result

    q = collections.deque([root])

    while q:
        level_size = len(q)
        current_level = []
        for _ in range(level_size):
            node = q.popleft()
            current_level.append(node.val)
            if node.left:
                q.append(node.left)
            if node.right:
                q.append(node.right)
        result.append(current_level)
        
    return result
