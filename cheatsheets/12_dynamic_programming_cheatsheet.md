
# Cheatsheet: Dynamic Programming (Intro)

**Core Concept:** An optimization technique for recursive problems that have **overlapping subproblems**. It works by storing the results of subproblems to avoid re-computation.

**Mantra:** "Don't re-calculate what you've already solved."

---

### Two Main Approaches

| Approach | Method | How it Works |
|:---|:---|:---|
| **Memoization** | Top-Down (Recursive) | A standard recursive function that is enhanced with a cache (dict/array). Before computing, it checks the cache. After computing, it stores the result in the cache. |
| **Tabulation** | Bottom-Up (Iterative) | Build a table (`dp` array) starting from the base cases and iteratively compute all solutions up to the final target. |

---

### Identifying DP Problems

- Look for keywords like "find the number of ways", "find the minimum/maximum cost/value/path", "find the optimal way".
- The problem can be defined as a function of its subproblems, e.g., `F(n) = F(n-1) + F(n-2)`.

---

### Classic Example: Climbing Stairs / Fibonacci

- **Problem:** Find the number of ways to climb `n` stairs, taking 1 or 2 steps at a time.
- **Recurrence Relation:** `ways(n) = ways(n-1) + ways(n-2)`
- **Tabulation Solution (O(1) space):**

```python
if n <= 1: return 1
one_step_back = 1
two_steps_back = 1
for _ in range(2, n + 1):
    current = one_step_back + two_steps_back
    two_steps_back = one_step_back
    one_step_back = current
return one_step_back
```
