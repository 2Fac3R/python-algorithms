# Cheatsheet: Python Fundamentals for Problem Solving

A quick reference for core Python concepts used in algorithms and data structures.

---
### Data Structures & Mutability

| Structure | Type | Mutable? | Key Use Case |
|:---|:---|:---|:---|
| **List** | `[1, 2]` | Yes | Ordered sequences, stacks. |
| **Tuple** | `(1, 2)` | No | Immutable data, dictionary keys. |
| **Dictionary**| `{'a': 1}`| Yes | Key-value mapping, O(1) lookup. |
| **Set** | `{1, 2}` | Yes | Storing unique items, O(1) membership tests. |

---
### Essential Built-in Functions

| Function | Example | Description |
|:---|:---|:---|
| `len(c)` | `len([1,2])` -> `2` | Get length of a collection. |
| `enumerate(c)`| `for i, v in enumerate(l):` | Get index and value during iteration. |
| `sorted(c)` | `sorted([3,1,2])` -> `[1,2,3]` | **Returns a new** sorted list. |
| `c.sort()` | `l.sort()` | Sorts a list **in-place**. |

---
### Common String Methods

| Method | Example | Result/Use |
|:---|:---|:---|
| `.lower()`/`.upper()`| `'Hi'.lower()` -> `'hi'` | Case-insensitive comparison. |
| `.split(d)` | `'a-b'.split('-')` -> `['a','b']` | String to List. |
| `.join(c)` | `'-'.join(['a','b'])` -> `'a-b'` | List of strings to String. |
| `.isalnum()` | `'a1'.isalnum()` -> `True` | Check if all are letters or numbers. |

---
### The `collections` Module

| Tool | Purpose | Example |
|:---|:---|:---|
| **`deque`** | Fast queue with O(1) `append` & `popleft`. | `from collections import deque` |
| **`defaultdict`**| Auto-initializes missing keys. | `defaultdict(int)` # default is 0 |
| **`Counter`** | Fast frequency counting. | `Counter('apple')` # `{'a':1...}` |

---
### Comprehensions

A concise way to create collections from iterables.

- **List:** `[x*x for x in range(5)]`
- **Set:** `{x*x for x in [1,2,2]}` -> `{1, 4}`
- **Dict:** `{x: x*x for x in range(3)}`

---
### Error Handling & Type Hinting

**Basic Error Handling:**
```python
try:
    x = 1 / 0
except ZeroDivisionError:
    print("Cannot divide by zero!")
```

**Common Type Hints:**
- Primitives: `name: str`, `age: int`, `is_valid: bool`
- Collections: `from typing import List, Dict, Optional`
  - `nums: List[int]`
  - `counts: Dict[str, int]`
  - `node: Optional[ListNode]` (means it can be `ListNode` or `None`)

---
### Class Basics (OOP)

A blueprint for creating objects. Essential for Trees, Linked Lists, etc.
```python
class TreeNode:
    # The constructor, called when creating an object.
    def __init__(self, val=0, left=None, right=None):
        # `self` is the instance of the object.
        # `self.val` is an attribute (instance variable).
        self.val = val
        self.left = left
        self.right = right
```