
# Solutions: Exam - Advanced Graph Algorithms

---

### Question 1 (Concept)

What kind of graph is required for a topological sort to be possible, and what does it signify if a valid topological sort cannot be produced?

- **Required Graph Type:** A Directed Acyclic Graph (DAG).
- **Significance of Failure:** It signifies that the graph contains at least one cycle.

---

### Question 2 (Application)

Which algorithm would you use to find the fastest route between two cities in a road network where the travel time between cities is known?

- **Correct Answer:** d) Dijkstra's Algorithm
- **Explanation:** This is a classic single-source shortest path problem on a weighted graph.

---

### Question 3 (Data Structures)

What auxiliary data structure is essential for an efficient implementation of Dijkstra's algorithm, and what does it store?

- **Data Structure:** A Min-Heap (or Min-Priority Queue).
- **It Stores:** Tuples of `(distance, node)`, allowing the algorithm to always process the node that is currently closest to the source.

---

### Question 4 (Algorithm Logic)

In Kahn's algorithm for topological sort, which nodes are the very first ones to be added to the queue?

- **Answer:** All nodes with an in-degree of 0.
- **Explanation:** These are the nodes that have no prerequisites or dependencies.

