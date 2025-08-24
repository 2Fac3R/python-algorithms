
# Algorithmic Paradigm: Dynamic Programming (Intro)

**Dynamic Programming (DP)** is an advanced optimization technique for solving complex problems by breaking them down into a collection of simpler, **overlapping subproblems**. The results of these subproblems are stored (or "memoized") to avoid redundant calculations.

DP is typically used for optimization problems (find the minimum, maximum, or number of ways to do something).

### Two Key Properties of DP Problems

For a problem to be solvable with DP, it must exhibit two properties:

1.  **Overlapping Subproblems:** The problem can be broken down into subproblems that are reused multiple times. The classic example is the Fibonacci sequence. To calculate `fib(5)`, you need `fib(4)` and `fib(3)`. To calculate `fib(4)`, you need `fib(3)` and `fib(2)`. The calculation for `fib(3)` is repeated.
2.  **Optimal Substructure:** The optimal solution to the overall problem can be constructed from the optimal solutions of its subproblems.

---

## Two Main Approaches to DP

### 1. Memoization (Top-Down)

This is a recursive approach. You write the standard recursive solution for the problem, but you add a cache (usually a hash map or an array) to store the results of subproblems. Before any computation, you check if the result for the current state is already in the cache. If it is, you return the cached value. If not, you compute it, store it in the cache, and then return it.

- **Pros:** Often more intuitive to write as it follows the natural recursive structure.
- **Cons:** Can lead to `RecursionError` if the recursion depth is too large.

**Template (Memoization):**
```python
cache = {}
def solve(n):
    if n in cache:
        return cache[n]
    if base_case(n):
        return ...
    
    result = solve(n-1) + ... # Recursive step
    cache[n] = result
    return result
```

### 2. Tabulation (Bottom-Up)

This is an iterative approach. You build a table (usually a 1D or 2D array, often called `dp`) from the "bottom up". You start by filling in the solutions for the smallest subproblems (the base cases) and then iteratively build up to the solution for the main problem.

- **Pros:** Generally more efficient as it avoids recursion overhead. No risk of stack overflow.
- **Cons:** Can sometimes be less intuitive to formulate as you need to figure out the correct order to fill the table.

**Template (Tabulation):**
```python
dp = [0] * (n + 1)
dp[0] = base_case_value_0
dp[1] = base_case_value_1

for i in range(2, n + 1):
    dp[i] = dp[i-1] + dp[i-2] # Iterative calculation

return dp[n]
```
