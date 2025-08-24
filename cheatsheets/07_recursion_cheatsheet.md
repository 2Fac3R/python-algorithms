
# Cheatsheet: Recursion

**Core Concept:** A function that calls itself to solve smaller, self-similar versions of the same problem.

---

### Anatomy of a Recursive Function

| Component | Purpose | Example (Factorial) |
|:---|:---|:---|
| **Base Case** | The condition that **stops** the recursion. | `if n <= 1: return 1` |
| **Recursive Step** | The function calls itself with a smaller input. | `return n * factorial(n-1)` |

---

### Key Mantra

1.  **Solve the Base Case:** Figure out the simplest possible input and its direct answer.
2.  **Assume the Recursive Leap of Faith:** Assume your function already works for a smaller version of the problem (e.g., `my_func(n-1)`).
3.  **Solve the Current Case:** Use the result from the smaller version to solve the current one.

---

### The Call Stack

- Each recursive call adds a frame to the call stack.
- This uses memory! Space complexity is often O(n) for simple recursion due to the stack depth.
- **Warning:** If the recursion is too deep (no base case or a very distant one), you will get a `RecursionError` (Stack Overflow).

---

### Common Problems Solved with Recursion

- Factorial, Fibonacci Sequence
- String/List Reversal & Manipulation
- **Tree and Graph Traversals (DFS)**
- **Backtracking Algorithms**
- Divide and Conquer Algorithms (Merge Sort)
