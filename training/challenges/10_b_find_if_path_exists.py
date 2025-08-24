
from typing import List

"""
Challenge: Find if Path Exists in Graph

There is a bi-directional graph with `n` vertices, where each vertex is labeled from `0` to `n - 1`. The edges in the graph are given as a 2D integer array `edges`, where each `edges[i] = [ui, vi]` denotes a bi-directional edge between vertex `ui` and vertex `vi`.

Given the `edges`, and two integers `source` and `destination`, return `true` if there is a valid path from `source` to `destination`, or `false` otherwise.

Technique:
This is a fundamental graph traversal problem. First, you must build a representation of the graph from the edge list, an **Adjacency List** is best. Then, start a traversal (either DFS or BFS) from the `source` node. Keep track of `visited` nodes to avoid cycles. If you ever encounter the `destination` node during the traversal, a path exists.
"""

def validPath(n: int, edges: List[List[int]], source: int, destination: int) -> bool:
    # Your implementation here
    pass

# --- Tests ---
def run_tests():
    test_cases = [
        (3, [[0,1],[1,2],[2,0]], 0, 2, True),
        (6, [[0,1],[0,2],[3,5],[5,4],[4,3]], 0, 5, False),
        (1, [], 0, 0, True)
    ]

    for i, (n, edges, source, dest, expected) in enumerate(test_cases):
        result = validPath(n, edges, source, dest)
        if result == expected:
            print(f"Test Case {i + 1}: PASSED")
        else:
            print(f"Test Case {i + 1}: FAILED. Expected {expected}, got {result}")

if __name__ == "__main__":
    run_tests()
