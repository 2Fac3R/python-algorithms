
# Technique: Linked List Manipulation

A Linked List is a fundamental linear data structure made of a chain of nodes, where each node contains a value and a pointer (or reference) to the next node in the chain. The last node points to `None`.

Unlike arrays, linked lists are not stored in contiguous memory locations, which gives them advantages in insertions and deletions but disadvantages in lookups.

### Python Node Implementation

```python
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
```

---

## Core Manipulation Patterns

### 1. Iterative Traversal with Pointers

This is the most basic pattern. You use a `current` pointer to traverse the list from the `head` to the end.

```python
current = head
while current:
    # do something with current.val
    current = current.next
```

### 2. The "Previous" and "Current" Pointer Pattern

To modify the list, especially for reversal, you need to keep track of not just the current node, but also the one before it (`prev`). This allows you to change the direction of the `next` pointers.

**Use Case:** Reversing a Linked List.

### 3. Two Pointers (Fast & Slow)

This is the same Two Pointers technique from arrays, but applied to linked lists. A `slow` pointer moves one step at a time, while a `fast` pointer moves two steps at a time.

**Use Cases:**
- **Cycle Detection:** If the `fast` pointer ever catches up to the `slow` pointer, there is a cycle.
- **Finding the Middle:** When the `fast` pointer reaches the end of the list, the `slow` pointer will be at the middle.

### 4. Dummy Head Node (Sentinel Node)

When building a new list or modifying the head of an existing one, it's often easier to use a `dummy` (or `sentinel`) node. This is a placeholder node that comes before the actual head of the list. It simplifies edge cases, like inserting into an empty list, because you always have a node to append to (`dummy.next`). You return `dummy.next` at the end.

**Use Case:** Merging two sorted lists.
