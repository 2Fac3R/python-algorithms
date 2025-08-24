
from typing import Optional

# Definition for a binary tree node, provided for all tree problems.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

"""
Challenge: Maximum Depth of Binary Tree

Given the `root` of a binary tree, return its maximum depth.

A binary tree's maximum depth is the number of nodes along the longest path from the root node down to the farthest leaf node.

Technique:
This is a classic problem to solve with recursion (a form of DFS). The logic follows the definition of depth itself.
"""

def maxDepth(root: Optional[TreeNode]) -> int:
    # Your implementation here
    pass

# --- Tests ---
def run_tests():
    # Test Case 1: [3,9,20,null,null,15,7] -> Expected 3
    root1 = TreeNode(3)
    root1.left = TreeNode(9)
    root1.right = TreeNode(20)
    root1.right.left = TreeNode(15)
    root1.right.right = TreeNode(7)
    
    # Test Case 2: [1,null,2] -> Expected 2
    root2 = TreeNode(1)
    root2.right = TreeNode(2)

    # Test Case 3: [] -> Expected 0
    root3 = None

    test_cases = [
        (root1, 3),
        (root2, 2),
        (root3, 0),
    ]

    for i, (root, expected) in enumerate(test_cases):
        result = maxDepth(root)
        if result == expected:
            print(f"Test Case {i + 1}: PASSED")
        else:
            print(f"Test Case {i + 1}: FAILED. Expected {expected}, got {result}")

if __name__ == "__main__":
    run_tests()
