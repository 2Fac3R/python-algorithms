
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

```python
# Visual Logic

String: { [ ( ) ] }

Stack: | { | -> | { [ | -> | { [ ( | -> | { [ | -> | { | -> |   |
       Push  Push    Push      Pop       Pop      Pop    (valid)
```

**Advanced Use Case: Min Stack**
- **Problem:** Get stack minimum in O(1) time.
- **Solution:** Use a second stack to store the current minimum at each level.

**Complexity:** `Time: O(n)`, `Space: O(n)` (in the worst case, e.g., `((((...))))`)
