
# Cheatsheet: Graphs

**Core Concept:** A data structure of nodes (vertices) connected by edges. Used to model networks.

---

### Representation: Adjacency List (Most Common)

A dictionary where keys are nodes and values are lists of their neighbors.

```python
# For edges (A,B), (A,C), (B,D)
graph = {
    'A': ['B', 'C'],
    'B': ['A', 'D'],
    'C': ['A'],
    'D': ['B']
}
```

---

### Crucial Tip: The `visited` Set

To traverse a graph, you **must** use a `visited` set to keep track of nodes you have already seen. This prevents your algorithm from getting stuck in an infinite loop if the graph has cycles.

```python
visited = set()

def dfs(node):
    if node in visited:
        return
    visited.add(node)
    # ... process node ...
    for neighbor in graph[node]:
        dfs(neighbor)
```

---

### Traversal Algorithms

| Algorithm | Data Structure | Key Feature | Common Use Case |
|:---|:---|:---|:---|
| **DFS** | Stack (Recursion) | Explores deeply down one path. | Pathfinding, cycle detection, topological sort. |
| **BFS** | Queue (`deque`) | Explores layer by layer. | Finding the **shortest path** in an **unweighted** graph. |
