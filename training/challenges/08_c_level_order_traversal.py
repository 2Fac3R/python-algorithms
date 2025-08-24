
from typing import Optional, List
import collections

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

"""
Challenge: Binary Tree Level Order Traversal

Given the `root` of a binary tree, return the level order traversal of its nodes' values. (i.e., from left to right, level by level).

Technique:
This is the classic problem for demonstrating **Breadth-First Search (BFS)**. A **queue** is the perfect data structure to keep track of the nodes to visit at each level.
"""

def levelOrder(root: Optional[TreeNode]) -> List[List[int]]:
    # Your implementation here
    pass

# --- Tests ---
def run_tests():
    # Test Case 1: [3,9,20,null,null,15,7] -> [[3],[9,20],[15,7]]
    root1 = TreeNode(3)
    root1.left = TreeNode(9)
    root1.right = TreeNode(20)
    root1.right.left = TreeNode(15)
    root1.right.right = TreeNode(7)
    
    # Test Case 2: [1] -> [[1]]
    root2 = TreeNode(1)

    # Test Case 3: [] -> []
    root3 = None

    test_cases = [
        (root1, [[3],[9,20],[15,7]]),
        (root2, [[1]]),
        (root3, []),
    ]

    for i, (root, expected) in enumerate(test_cases):
        result = levelOrder(root)
        if result == expected:
            print(f"Test Case {i + 1}: PASSED")
        else:
            print(f"Test Case {i + 1}: FAILED. Expected {expected}, got {result}")

if __name__ == "__main__":
    run_tests()
