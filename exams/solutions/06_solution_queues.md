
# Solutions: Exam - Queues (FIFO)

---

### Question 1 (Concept)

A queue follows the FIFO principle. What does FIFO stand for?

- **Answer:** First-In, First-Out.

---

### Question 2 (Implementation)

Why is `collections.deque` preferred over a standard Python `list` for implementing a queue?

- **Reason:** Because `collections.deque` provides an O(1) `popleft()` operation, which is very fast. A standard list's `pop(0)` is an O(n) operation, which is very slow as all other elements must be shifted.

---

### Question 3 (Code Logic)

Using `collections.deque`, which methods correspond to the following queue operations?

- **Enqueue (add an item):** `my_deque.append()`
- **Dequeue (remove an item):** `my_deque.popleft()`

---

### Question 4 (Application)

What fundamental graph/tree traversal algorithm relies on a queue to explore nodes layer by layer?

- **Answer:** Breadth-First Search (BFS).

