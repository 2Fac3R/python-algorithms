
from typing import List
import collections
import heapq

"""
Solution for: Network Delay Time
"""

def networkDelayTime(times: List[List[int]], n: int, k: int) -> int:
    """
    This solution uses Dijkstra's algorithm to find the shortest time from the source `k`
    to all other nodes.

    1.  **Build Adjacency List:** We build a graph where keys are nodes and values are lists
        of `(neighbor, weight)` tuples.
    2.  **Initialize:** 
        - A `distances` dictionary to store the shortest time to each node, initialized to infinity.
        - A min-priority queue (`min_heap`) to store `(time, node)` tuples. We start by
          pushing `(0, k)`.
    3.  **Process Heap:** While the heap is not empty, we pop the node with the shortest time.
    4.  **Explore Neighbors:** For each neighbor of the current node, we calculate the potential
        new time to reach it. If this new time is shorter than any previously found time,
        we update our `distances` and push the `(new_time, neighbor)` to the heap.
    5.  **Find Max Distance:** After the algorithm finishes, `distances` holds the shortest
        times to all reachable nodes. The time it takes for the signal to reach all nodes
        is the maximum of these shortest times.
    6.  **Check Reachability:** If the number of nodes in our `distances` map is less than `n`,
        it means some nodes were unreachable, so we return -1.
    """
    # 1. Build Adjacency List
    adj_list = collections.defaultdict(list)
    for u, v, w in times:
        adj_list[u].append((v, w))

    # 2. Initialize
    min_heap = [(0, k)] # (time, node)
    visited = set()
    max_time = 0

    # 3. Process Heap
    while min_heap:
        time, node = heapq.heappop(min_heap)

        if node in visited:
            continue
        
        visited.add(node)
        max_time = max(max_time, time)

        # 4. Explore Neighbors
        for neighbor, weight in adj_list[node]:
            if neighbor not in visited:
                heapq.heappush(min_heap, (time + weight, neighbor))

    # 5. Check Reachability
    return max_time if len(visited) == n else -1
