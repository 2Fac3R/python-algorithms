
# Data Structure: Heaps (Priority Queues)

A **Heap** (or Montículo) is a specialized tree-based data structure that satisfies the "heap property". It is a powerful way to implement a **Priority Queue**, which is an abstract data type where each element has a "priority" associated with it. 

Unlike a regular queue (FIFO) or stack (LIFO), a priority queue dequeues elements in order of their priority.

### The Heap Property

There are two main types of heaps:

1.  **Min-Heap:** The value of each parent node is **less than or equal to** the value of its children. This means the **smallest element** is always at the root of the tree.
2.  **Max-Heap:** The value of each parent node is **greater than or equal to** the value of its children. This means the **largest element** is always at the root.

**Important:** A heap is **not** a sorted structure. It only guarantees the relationship between parents and children, not between siblings or cousins.

### Python's `heapq` Module

Python provides the `heapq` module, which implements a **min-heap** using a standard Python `list`.

#### Key `heapq` Functions

- **`heapq.heappush(heap, item)`:** Pushes an item onto the heap, maintaining the heap property. **Time Complexity: O(log n)**.
- **`heapq.heappop(heap)`:** Pops and returns the **smallest** item from the heap. **Time Complexity: O(log n)**.
- **`heapq.heapify(list)`:** Transforms a regular list into a heap **in-place**. This is a very efficient operation. **Time Complexity: O(n)**.
- **Accessing the Smallest Item:** Since it's a min-heap, the smallest item is always the first element. You can peek at it with `heap[0]`. **Time Complexity: O(1)**.

### Simulating a Max-Heap with `heapq`

Since `heapq` is a min-heap, a common interview trick is to store **negative numbers** to simulate a max-heap. If you want to find the largest element, you store all numbers as negatives, and the "smallest" number popped from the min-heap (`-10`) will correspond to the largest actual number (`10`).

### Common Use Cases

- **Top K Problems:** Finding the "Kth largest/smallest element" or the "Top K frequent elements".
- **Scheduling:** Managing tasks by priority.
- **Pathfinding Algorithms:** Used in algorithms like Dijkstra's or A* to efficiently select the next node to visit.
