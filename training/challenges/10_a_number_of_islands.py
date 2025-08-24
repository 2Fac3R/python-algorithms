
from typing import List

"""
Challenge: Number of Islands

Given an `m x n` 2D binary grid `grid` which represents a map of '1's (land) and '0's (water), return the number of islands.

An island is surrounded by water and is formed by connecting adjacent lands horizontally or vertically. You may assume all four edges of the grid are all surrounded by water.

Technique:
This is a classic graph traversal problem where the graph is implicit. You can think of each '1' as a node and adjacent '1's as having an edge between them. Iterate through each cell of the grid. If you find a '1', you have found a new island. Increment your island count and then start a traversal (DFS or BFS) from that cell to find all connected parts of the island, marking them as visited (e.g., by changing them to '0') so you don't count them again.
"""

def numIslands(grid: List[List[str]]) -> int:
    # Your implementation here
    pass

# --- Tests ---
def run_tests():
    test_cases = [
        (
            [
              ["1","1","1","1","0"],
              ["1","1","0","1","0"],
              ["1","1","0","0","0"],
              ["0","0","0","0","0"]
            ], 1
        ),
        (
            [
              ["1","1","0","0","0"],
              ["1","1","0","0","0"],
              ["0","0","1","0","0"],
              ["0","0","0","1","1"]
            ], 3
        ),
    ]

    for i, (grid, expected) in enumerate(test_cases):
        # Create a deep copy for each test run
        grid_copy = [list(row) for row in grid]
        result = numIslands(grid_copy)
        if result == expected:
            print(f"Test Case {i + 1}: PASSED")
        else:
            print(f"Test Case {i + 1}: FAILED. Expected {expected}, got {result}")

if __name__ == "__main__":
    run_tests()
