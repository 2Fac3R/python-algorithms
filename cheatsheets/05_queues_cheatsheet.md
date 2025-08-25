
# Cheatsheet: Queues (FIFO)

**Core Concept:** A First-In, First-Out (FIFO) data structure. The first item you add is the first one you can take out.

**When to Use:**
- Processing items in the order they were received.
- Breadth-First Search (BFS).
- Task scheduling, simulations.

---

### Implementation in Python

Use `collections.deque` for efficiency.

| Operation | Method | Description |
|:---|:---|:---|
| **Enqueue** | `my_q.append(item)` | Adds to the back. |
| **Dequeue** | `my_q.popleft()` | **O(1)** - Removes from the front. |
| **Peek** | `my_q[0]` | Views the front item. |
| **Check Empty** | `if not my_q:` | Checks if the queue is empty. |

**Warning:** Do not use `list.pop(0)` for dequeue, it is an O(n) operation and very slow.

---

### Classic Problem: Breadth-First Search (BFS)

**Logic:** Use a queue to visit nodes layer by layer. Add neighbors to the queue and use a `visited` set to avoid cycles.

**Implementation Snippet:**
```python
queue = deque([start_node])
visited = {start_node}
while queue:
    node = queue.popleft()
    # ... process node ...
    for neighbor in get_neighbors(node):
        if neighbor not in visited:
            visited.add(neighbor)
            queue.append(neighbor)
```

**Complexity:** `Time: O(n)` (for BFS), `Space: O(n)` (to store nodes in the queue)
