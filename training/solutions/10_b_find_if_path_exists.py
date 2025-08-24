
from typing import List
import collections

"""
Solution for: Find if Path Exists in Graph
"""

def validPath(n: int, edges: List[List[int]], source: int, destination: int) -> bool:
    """
    This solution uses Breadth-First Search (BFS) to find a path.

    1.  **Build Adjacency List:** First, we convert the `edges` list into a more usable
        graph representation, an adjacency list. This is a dictionary where each key is a
        node and its value is a list of its neighbors.
    2.  **Initialize for BFS:** We create a `visited` set to keep track of nodes we've
        already seen to avoid infinite loops in case of cycles. We also initialize a
        `queue` with the `source` node.
    3.  **Perform BFS:**
        - While the queue is not empty, we dequeue a node.
        - If this node is our `destination`, we've found a path, so we return `True`.
        - We then look at all of its `neighbors`. For any neighbor we haven't visited yet,
          we add it to the `visited` set and enqueue it for future processing.
    4.  **No Path Found:** If the BFS completes (the queue becomes empty) and we never
        reached the destination, it means no path exists. We return `False`.
    """
    if source == destination:
        return True

    # 1. Build Adjacency List
    adj_list = collections.defaultdict(list)
    for u, v in edges:
        adj_list[u].append(v)
        adj_list[v].append(u)

    # 2. Initialize for BFS
    visited = {source}
    queue = collections.deque([source])

    # 3. Perform BFS
    while queue:
        node = queue.popleft()
        
        for neighbor in adj_list[node]:
            if neighbor == destination:
                return True
            if neighbor not in visited:
                visited.add(neighbor)
                queue.append(neighbor)

    # 4. No Path Found
    return False
