
# Cheatsheet: Heaps (Priority Queues)

**Core Concept:** A tree-based data structure that keeps the smallest (min-heap) or largest (max-heap) element at the root for fast O(1) peeking.

**When to Use:**
- Problems involving finding the "Top K" or "Kth Largest/Smallest" elements.
- Implementing priority queues for scheduling or simulations.
- Graph algorithms like Dijkstra's.

---

### Python `heapq` Module (implements a Min-Heap)

| Operation | Method | Complexity | Description |
|:---|:---|:---|:---|
| **Push** | `heapq.heappush(h, item)` | O(log n) | Adds an item, maintaining the heap. |
| **Pop** | `heapq.heappop(h)` | O(log n) | Removes and returns the **smallest** item. |
| **Peek Smallest** | `h[0]` | O(1) | Views the smallest item without removing it. |
| **Heapify** | `heapq.heapify(list)` | O(n) | Converts a list to a heap **in-place**. |

---

### Max-Heap Trick

- **Problem:** You need a max-heap, but `heapq` is a min-heap.
- **Solution:** Store the **negative** of your numbers. The "smallest" number in the min-heap will correspond to the largest absolute number.

```python
# To get the two largest items
max_heap = [-5, -10, -2]
heapq.heapify(max_heap) # heap is now [-10, -5, -2]

largest = -heapq.heappop(max_heap) # largest is 10
second_largest = -heapq.heappop(max_heap) # second_largest is 5
```
