
from typing import List

"""
Solution for: Number of Islands
"""

def numIslands(grid: List[List[str]]) -> int:
    """
    This solution iterates through each cell of the grid. When it finds a cell
    containing '1' (land), it increments the island count and starts a Depth-First Search (DFS)
    to find and "sink" all parts of that island by changing their value to '0'.
    This prevents us from counting the same island multiple times.
    """
    if not grid:
        return 0

    rows, cols = len(grid), len(grid[0])
    island_count = 0

    def dfs(r, c):
        # Base cases for stopping the DFS:
        # 1. Out of bounds (row or col)
        # 2. Current cell is water ('0')
        if r < 0 or c < 0 or r >= rows or c >= cols or grid[r][c] == '0':
            return

        # Mark the current cell as visited by sinking it
        grid[r][c] = '0'

        # Explore all 4 directions
        dfs(r + 1, c)
        dfs(r - 1, c)
        dfs(r, c + 1)
        dfs(r, c - 1)

    for r in range(rows):
        for c in range(cols):
            if grid[r][c] == '1':
                island_count += 1
                dfs(r, c) # Start DFS to find and sink the entire island
    
    return island_count
