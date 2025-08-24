
# Cheatsheet: Advanced Graph Algorithms

---

### 1. Topological Sort (Kahn's Algorithm)

-   **What it is:** A linear ordering of nodes in a **Directed Acyclic Graph (DAG)** where for every edge `u -> v`, `u` comes before `v`.
-   **Use Case:** Task scheduling, course prerequisites, dependency resolution.
-   **Key Idea:** Use a **queue** and track the **in-degree** (number of incoming edges) of each node.

**Algorithm:**
1.  Build adjacency list and calculate all in-degrees.
2.  Add all nodes with an in-degree of `0` to a queue.
3.  While queue is not empty:
    a. Dequeue a node, add it to the result.
    b. For its neighbors, decrement their in-degree.
    c. If a neighbor's in-degree becomes `0`, enqueue it.
4.  If `len(result) == num_nodes`, a valid sort exists. Otherwise, there is a cycle.

---

### 2. Dijkstra's Algorithm

-   **What it is:** Finds the shortest path from a single source to all other nodes in a **weighted graph**.
-   **Use Case:** GPS navigation, network routing.
-   **Requirement:** All edge weights must be **non-negative**.
-   **Key Idea:** Use a **min-priority queue (min-heap)** to always explore the path with the smallest current distance from the source.

**Algorithm:**
1.  Create `distances` map, initialized to infinity (source is 0).
2.  Push `(0, source_node)` to a min-heap.
3.  While heap is not empty:
    a. Pop the `(dist, node)` with the smallest `dist`.
    b. If `dist` is greater than the known `distances[node]`, continue (stale path).
    c. For each neighbor, if a shorter path is found via the current node, update `distances[neighbor]` and push the new `(new_dist, neighbor)` to the heap.
