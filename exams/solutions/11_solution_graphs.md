
# Solutions: Exam - Graphs

---

### Question 1 (Representation)

What is the most common way to represent a graph in a coding interview, and what is its main advantage for sparse graphs (graphs with relatively few edges)?

- **Method:** Adjacency List.
- **Advantage:** It is space-efficient, as it only stores the edges that actually exist.

---

### Question 2 (Concept)

When traversing a graph, what is the primary purpose of using a `visited` set?

- **Correct Answer:** c) To prevent getting stuck in infinite loops in graphs with cycles.
- **Explanation:** Without tracking visited nodes, a traversal could go back and forth between two nodes forever.

---

### Question 3 (Application)

If you need to find the shortest path (in terms of number of edges) between two nodes in an **unweighted** graph, which traversal algorithm should you always choose?

- **Answer:** Breadth-First Search (BFS).
- **Explanation:** BFS explores the graph layer by layer, guaranteeing that it will find the path with the fewest edges first.

---

### Question 4 (Analysis)

Given the following adjacency list for an undirected graph:
`graph = {0: [1], 1: [0, 2], 2: [1], 3: [4], 4: [3]}`

Is there a path between node `0` and node `4`?

- **Answer (Yes/No):** No.
- **Explanation:** The graph has two disconnected components: one containing nodes {0, 1, 2} and another containing nodes {3, 4}. There are no edges connecting these two components.

