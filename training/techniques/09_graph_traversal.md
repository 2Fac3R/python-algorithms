
# Data Structure: Graphs

A **Graph** is a non-linear data structure consisting of a set of **vertices** (or nodes) and a set of **edges** that connect pairs of vertices. It is the most general data structure and can be used to model any kind of network, from social networks to road maps.

### Core Terminology

- **Vertex (Node):** A point or node in the graph.
- **Edge:** A connection between two vertices.
- **Undirected Graph:** Edges have no orientation. The edge (A, B) is the same as (B, A).
- **Directed Graph (Digraph):** Edges have a direction. The edge (A, B) goes from A to B, but not necessarily from B to A.
- **Weighted Graph:** Each edge has a weight or cost associated with it.
- **Cycle:** A path in a graph that starts and ends at the same vertex.

---

## Graph Representation

How you store a graph in code is crucial. The most common way in interviews is an Adjacency List.

### 1. Adjacency List (Most Common)

You use a hash map (dictionary) where each key is a vertex, and its value is a list of all the vertices it is connected to (its neighbors).

**Example (Undirected Graph):**
```python
# A is connected to B and C
# B is connected to A
# C is connected to A
graph = {
    'A': ['B', 'C'],
    'B': ['A'],
    'C': ['A']
}
```
- **Pros:** Space-efficient for sparse graphs (graphs with few edges). Easy to iterate over the neighbors of a node.
- **Cons:** Checking for the existence of a specific edge (A, B) can take O(k) time, where k is the number of neighbors of A.

### 2. Adjacency Matrix

A 2D array (list of lists) where `matrix[i][j] = 1` if there is an edge between vertex `i` and vertex `j`, and `0` otherwise.
- **Pros:** Checking for a specific edge is very fast, O(1).
- **Cons:** Uses a lot of space, O(V²), where V is the number of vertices. Inefficient for sparse graphs.

---

## Graph Traversal

Traversal algorithms are the same as for trees, but with one **critical addition**: you must keep track of visited nodes to avoid infinite loops in graphs with cycles.

- **`visited` set:** A hash set is used to store the nodes that have already been visited. Before visiting a node, you check if it's in the `visited` set. If it is, you ignore it. If not, you visit it and add it to the set.

**Code Example (DFS Traversal with `visited` set):**
```python
graph = { ... } # Adjacency list
visited = set()

def dfs(node):
    if node in visited:
        return
    
    visited.add(node)
    print(node) # Process node

    for neighbor in graph[node]:
        dfs(neighbor)

dfs(starting_node)
```

- **Depth-First Search (DFS):** Explores as far as possible down one path before backtracking. Uses a **stack** (or recursion).
- **Breadth-First Search (BFS):** Explores layer by layer. Uses a **queue**.
