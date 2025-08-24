
# Cheatsheet: Linked List Manipulation

**Core Concept:** A data structure of nodes where each node points to the next. Unlike arrays, they excel at insertions/deletions but are slow for lookups (O(n)).

---

### `ListNode` Class

```python
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
```

---

### Core Patterns

| Pattern | Pointers Used | Key Use Case |
|:---|:---|:---|
| **Iterative Traversal** | `current` | Visiting each node. |
| **Prev & Current** | `prev`, `current`, `next_node` | Reversing a linked list. |
| **Fast & Slow** | `slow`, `fast` | Cycle detection, finding the middle node. |
| **Dummy Head Node** | `dummy`, `current` | Building a new list, merging lists. |

---

### Key Operations

**Reversing a List (Iterative):**
```python
prev = None
current = head
while current:
    next_temp = current.next
    current.next = prev
    prev = current
    current = next_temp
return prev # New head
```

**Cycle Detection (Floyd's Algorithm):**
```python
slow, fast = head, head
while fast and fast.next:
    slow = slow.next
    fast = fast.next.next
    if slow == fast:
        return True # Cycle detected
return False
```
