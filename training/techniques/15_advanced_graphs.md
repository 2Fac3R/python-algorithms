
# Technique: Advanced Graph Algorithms

Beyond basic traversal (DFS, BFS), there are several powerful algorithms for solving more complex problems on graphs. This guide covers two of the most essential: Topological Sort and Dijkstra's Algorithm.

---

## 1. Topological Sort

**Concept:** A topological sort is a **linear ordering** of the vertices in a **Directed Acyclic Graph (DAG)**. For every directed edge from vertex `u` to vertex `v`, vertex `u` must come before vertex `v` in the ordering.

**Use Case:** It's used to solve problems involving dependencies. The most common example is **task scheduling** or **course prerequisites**. If Course B depends on Course A, you must complete A before B. A topological sort gives you a valid sequence to complete all tasks.

**Requirement:** The graph **must be a DAG**. If the graph has a cycle, a topological sort is not possible (as there is a circular dependency).

### Kahn's Algorithm (BFS-based approach)

This is a common and intuitive algorithm for topological sorting:

1.  **Compute In-degrees:** For every vertex, count how many incoming edges it has. This is its "in-degree".
2.  **Initialize Queue:** Find all vertices with an in-degree of 0 and add them to a queue. These are the starting points with no prerequisites.
3.  **Process Queue:**
    -   While the queue is not empty, dequeue a vertex `u`.
    -   Add `u` to your sorted list (`result`).
    -   For each neighbor `v` of `u`:
        -   Decrement the in-degree of `v` (since we have now "completed" task `u`).
        -   If the in-degree of `v` becomes 0, add `v` to the queue.
4.  **Check for Cycles:** After the loop, if the length of your `result` list is equal to the total number of vertices in the graph, you have a valid topological sort. If it's smaller, the graph must have a cycle.

**Code Example (Kahn's Algorithm):**
```python
import collections

def topological_sort(num_nodes, edges):
    # 1. Build adjacency list and in-degree map
    adj_list = {i: [] for i in range(num_nodes)}
    in_degree = {i: 0 for i in range(num_nodes)}

    for start_node, end_node in edges:
        adj_list[start_node].append(end_node)
        in_degree[end_node] += 1

    # 2. Initialize queue with 0-in-degree nodes
    queue = collections.deque([node for node in in_degree if in_degree[node] == 0])
    
    topological_order = []

    # 3. Process queue
    while queue:
        node = queue.popleft()
        topological_order.append(node)

        for neighbor in adj_list[node]:
            in_degree[neighbor] -= 1
            if in_degree[neighbor] == 0:
                queue.append(neighbor)

    # 4. Check for cycle
    if len(topological_order) == num_nodes:
        return topological_order
    else:
        return [] # Cycle detected!
```

---

## 2. Dijkstra's Algorithm

**Concept:** Dijkstra's algorithm finds the **shortest path** from a single source node to all other nodes in a **weighted graph with non-negative edge weights**.

**Use Case:** Finding the fastest route in a GPS, network routing (finding the quickest path for data packets), etc.

### Algorithm Steps

1.  **Initialization:**
    -   Create a `distances` dictionary or array to store the shortest distance from the `source` to every other node. Initialize all distances to infinity, except for the source node, which is 0 (`distances[source] = 0`).
    -   Create a **min-priority queue** (a min-heap) to store tuples of `(distance, node)`. This will help us always explore the "closest" node next. Add `(0, source)` to the priority queue.
2.  **Process Queue:**
    -   While the priority queue is not empty, extract the `(dist, node)` with the smallest `dist`.
    -   If this `dist` is greater than the already known shortest distance to `node` (`distances[node]`), it means we found a shorter path to it earlier. We can skip this entry.
    -   For each `neighbor` of the current `node`:
        -   Calculate the new potential distance: `new_dist = dist + weight_of_edge(node, neighbor)`.
        -   If `new_dist` is less than the known distance to that neighbor (`distances[neighbor]`), we have found a new, shorter path.
        -   Update `distances[neighbor] = new_dist` and add `(new_dist, neighbor)` to the priority queue.
3.  **Result:** After the loop, the `distances` dictionary will contain the shortest path distances from the source to all reachable nodes.
