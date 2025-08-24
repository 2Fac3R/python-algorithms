
from typing import Optional

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

"""
Challenge: Validate Binary Search Tree

Given the `root` of a binary tree, determine if it is a valid binary search tree (BST).

A valid BST is defined as follows:
- The left subtree of a node contains only nodes with keys less than the node's key.
- The right subtree of a node contains only nodes with keys greater than the node's key.
- Both the left and right subtrees must also be binary search trees.

Technique:
A simple check of `root.left.val < root.val < root.right.val` is NOT enough. The entire subtree must satisfy the condition. The standard solution uses a recursive helper function that checks if each node's value is within a valid range `(min_val, max_val)`.
"""

def isValidBST(root: Optional[TreeNode]) -> bool:
    # Your implementation here
    pass

# --- Tests ---
def run_tests():
    # Test Case 1: [2,1,3] -> Valid
    root1 = TreeNode(2, TreeNode(1), TreeNode(3))
    
    # Test Case 2: [5,1,4,null,null,3,6] -> Invalid
    root2 = TreeNode(5)
    root2.left = TreeNode(1)
    root2.right = TreeNode(4)
    root2.right.left = TreeNode(3)
    root2.right.right = TreeNode(6)

    test_cases = [
        (root1, True),
        (root2, False),
    ]

    for i, (root, expected) in enumerate(test_cases):
        result = isValidBST(root)
        if result == expected:
            print(f"Test Case {i + 1}: PASSED")
        else:
            print(f"Test Case {i + 1}: FAILED. Expected {expected}, got {result}")

if __name__ == "__main__":
    run_tests()
