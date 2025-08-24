
from typing import List

"""
Challenge: Network Delay Time

You are given a network of `n` nodes, labeled from `1` to `n`. You are also given `times`, a list of travel times as directed edges `times[i] = (u, v, w)`, where `u` is the source node, `v` is the target node, and `w` is the time it takes for a signal to travel from source to target.

We will send a signal from a given node `k`. Return the minimum time it takes for all `n` nodes to receive the signal. If it is impossible for all `n` nodes to receive the signal, return -1.

Technique:
This is a classic "single-source shortest path" problem on a weighted, directed graph. The goal is to find the time it takes for the signal to reach the *farthest* node from the source `k`. This is a perfect application for **Dijkstra's Algorithm**.
"""

def networkDelayTime(times: List[List[int]], n: int, k: int) -> int:
    # Your implementation here
    pass

# --- Tests ---
def run_tests():
    test_cases = [
        ([[2,1,1],[2,3,1],[3,4,1]], 4, 2, 2),
        ([[1,2,1]], 2, 1, 1),
        ([[1,2,1]], 2, 2, -1),
    ]

    for i, (times, n, k, expected) in enumerate(test_cases):
        result = networkDelayTime(times, n, k)
        if result == expected:
            print(f"Test Case {i + 1}: PASSED")
        else:
            print(f"Test Case {i + 1}: FAILED. Expected {expected}, got {result}")

if __name__ == "__main__":
    run_tests()
