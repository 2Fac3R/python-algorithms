
from typing import List

"""
Challenge: Course Schedule

There are a total of `numCourses` courses you have to take, labeled from `0` to `numCourses - 1`. You are given an array `prerequisites` where `prerequisites[i] = [ai, bi]` indicates that you must take course `bi` first if you want to take course `ai`.

For example, the pair `[0, 1]` indicates that to take course `0` you have to first take course `1`.

Return `true` if you can finish all courses. Otherwise, return `false`.

Technique:
This is a classic graph problem about dependencies. It can be modeled as a directed graph where an edge `b -> a` exists if `a` is a prerequisite for `b`. The question "can you finish all courses?" is equivalent to asking "does this directed graph contain a cycle?". If there is a cycle (e.g., A -> B -> A), it's impossible. This can be solved efficiently with **Topological Sort**.
"""

def canFinish(numCourses: int, prerequisites: List[List[int]]) -> bool:
    # Your implementation here
    pass

# --- Tests ---
def run_tests():
    test_cases = [
        (2, [[1,0]], True),
        (2, [[1,0],[0,1]], False),
        (5, [[0,1],[0,2],[1,3],[1,4],[3,4]], True),
    ]

    for i, (n, prereqs, expected) in enumerate(test_cases):
        result = canFinish(n, prereqs)
        if result == expected:
            print(f"Test Case {i + 1}: PASSED")
        else:
            print(f"Test Case {i + 1}: FAILED. Expected {expected}, got {result}")

if __name__ == "__main__":
    run_tests()
