
from typing import Optional

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

"""
Solution for: Validate Binary Search Tree
"""

def isValidBST(root: Optional[TreeNode]) -> bool:
    """
    This solution uses a recursive helper function (DFS) to validate the tree.

    The helper function `validate(node, low, high)` checks if the current node's value
    is within the valid range `(low, high)`. Initially, this range is negative infinity
    to positive infinity.

    When we traverse to a node's LEFT child, we know its value must be less than the
    current node's value. So, we update the `high` boundary to be `node.val`.

    When we traverse to a node's RIGHT child, we know its value must be greater than the
    current node's value. So, we update the `low` boundary to be `node.val`.
    """
    
    def validate(node, low=-float('inf'), high=float('inf')):
        # Base Case: An empty tree is a valid BST.
        if not node:
            return True

        # Check if the current node's value is within the valid range.
        if not (low < node.val < high):
            return False

        # Recursively check the left and right subtrees with updated boundaries.
        return (validate(node.left, low, node.val) and
                validate(node.right, node.val, high))

    return validate(root)
