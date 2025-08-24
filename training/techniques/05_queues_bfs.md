
# Technique: Queues (FIFO)

A **Queue** is a linear data structure that follows the **FIFO (First-In, First-Out)** principle. This is like a queue of people waiting for a bus: the first person to join the queue is the first person to get on the bus.

In Python, the most efficient way to implement a queue is by using `collections.deque` (pronounced "deck"), which stands for "double-ended queue". It is optimized for fast appends and pops from both ends.

- **Enqueue (Add an item):** `queue.append(item)`
- **Dequeue (Remove an item):** `queue.popleft()`
- **Peek (Look at the front item):** `queue[0]` (if the queue is not empty)

Using a standard Python `list` is inefficient for this because `list.pop(0)` is an O(n) operation, as all subsequent elements need to be shifted.

## Core Properties

- **FIFO Principle:** The first element added to the queue will be the first one to be removed.
- **Key Operations:**
    - `enqueue`: Adds an element to the back (end) of the queue.
    - `dequeue`: Removes and returns the front element of the queue.
    - `peek` or `front`: Returns the front element without removing it.
    - `isEmpty`: Checks if the queue is empty.

## Why are they useful in interviews?

Queues are fundamental in algorithms that need to process items in the order they were received. Their most prominent application is in graph and tree traversal algorithms.

**Common Use Case: Breadth-First Search (BFS)**

BFS is a traversal algorithm that explores a graph or tree layer by layer. A queue is the perfect data structure to manage this.

1. Start with a root node. Add it to the queue.
2. While the queue is not empty:
   a. Dequeue a node.
   b. Process it (e.g., print its value).
   c. Enqueue all of its unvisited neighbors.

This ensures that you visit all nodes at the current "depth" or "layer" before moving on to the next one.

**Code Example (BFS loop):**
```python
from collections import deque

queue = deque([root_node])
visited = {root_node}

while queue:
    node = queue.popleft()
    # ... process node ...
    for neighbor in get_neighbors(node):
        if neighbor not in visited:
            visited.add(neighbor)
            queue.append(neighbor)
```

**Other Common Applications:**
- **Simulations:** Modeling any real-world queue, like a printer queue or requests to a server.
- **Task Scheduling:** Processing tasks in the order they were submitted.
- **Caching:** Implementing a simple LRU (Least Recently Used) cache.
