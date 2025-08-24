
from typing import Optional

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

"""
Solution for: Maximum Depth of Binary Tree
"""

def maxDepth(root: Optional[TreeNode]) -> int:
    """
    This solution uses recursion (DFS).

    - Base Case: If the current node (`root`) is None, it means we are at the end of a branch,
      so its depth is 0.
    
    - Recursive Step: If the node exists, its depth is 1 (for the node itself) plus the
      maximum of the depths of its left and right subtrees. We recursively call `maxDepth`
      on the left and right children to find their depths.
    """
    # Base Case
    if not root:
        return 0

    # Recursive Step
    left_depth = maxDepth(root.left)
    right_depth = maxDepth(root.right)

    return 1 + max(left_depth, right_depth)
