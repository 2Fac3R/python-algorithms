
# Cheatsheet: Stacks (LIFO)

**Core Concept:** A Last-In, First-Out (LIFO) data structure. The last item you add is the first one you can take out.

**When to Use:**
- Parsing nested structures (e.g., parentheses).
- Problems involving reversal or backtracking.
- Depth-First Search (DFS) iteratively.

---

### Implementation in Python

Use a standard `list`.

| Operation | Method | Description |
|:---|:---|:---|
| **Push** | `my_stack.append(item)` | Adds to the top. |
| **Pop** | `my_stack.pop()` | Removes from the top. |
| **Peek** | `my_stack[-1]` | Views the top item. |
| **Check Empty** | `if not my_stack:` | Checks if the stack is empty. |

---

### Classic Problem: Valid Parentheses

**Logic:** Use a map for brackets. If open, push to stack. If close, pop and check if it matches. After loop, stack must be empty.

**Implementation Snippet:**
```python
stack = []
bracket_map = { ")": "(", "}": "{", "]": "[" }
for char in s:
    if char in bracket_map.values():
        stack.append(char)
    elif char in bracket_map.keys():
        if not stack or stack.pop() != bracket_map[char]:
            return False
return not stack
```

**Advanced Use Case: Min Stack**
- **Problem:** Get stack minimum in O(1) time.
- **Solution:** Use a second stack to store the current minimum at each level.

**Complexity:** `Time: O(n)`, `Space: O(n)` (in the worst case, e.g., `((((...))))`)
