
# Solutions: Exam - Heaps (Priority Queues)

---

### Question 1 (Concept)

What is the fundamental guarantee provided by a **Min-Heap**?

- **Correct Answer:** b) The smallest element is always at the root (index 0).
- **Explanation:** A heap is not fully sorted. It only guarantees the parent-child relationship (parent <= child), which ensures the root is the minimum.

---

### Question 2 (Complexity)

What is the time complexity of `heapq.heappush()` and `heapq.heappop()`?

- **Answer:** O(log n)

---

### Question 3 (Implementation)

Python's `heapq` module provides a min-heap. How would you use it to simulate a **Max-Heap** to efficiently find the largest elements?

- **Answer:** By storing the **negative** of the numbers. The "smallest" element in the min-heap will correspond to the largest actual number.

---

### Question 4 (Application)

You need to find the 10th largest element from a stream of 1 million numbers. What is the most efficient way to use a heap for this, and what would be its size?

- **Method:** Use a **Min-Heap**.
- **Heap Size:** **10**.
- **Explanation:** Maintain a min-heap of size 10. For each new number, if it's larger than the smallest number in the heap (the root), replace the root with the new number. At the end, the root of the heap will be the 10th largest element.

