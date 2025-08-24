
# Technique: Recursion

A recursive function is a function that calls itself. It's a powerful technique for solving problems that can be broken down into smaller, self-similar subproblems.

To design a recursive function, you need two essential components:

### 1. Base Case

This is the condition that **stops the recursion**. It represents the simplest possible version of the problem that can be solved directly without further recursion. Without a base case, a recursive function would call itself infinitely, leading to a `RecursionError: maximum recursion depth exceeded` (a stack overflow).

**Example (Factorial):** The factorial of 1 (or 0) is 1. This is the simplest case.
`if n <= 1: return 1`

### 2. Recursive Step (or Recursive Case)

This is where the function calls itself, but with a modified argument that moves it closer to the base case. It's the part that breaks the problem down.

**Example (Factorial):** The factorial of `n` is `n` multiplied by the factorial of `n-1`. The problem `factorial(n-1)` is a smaller version of the original problem.
`return n * factorial(n - 1)`

**Full Example (Factorial):**
```python
def factorial(n):
    # Base Case: the simplest problem to solve
    if n <= 1:
        return 1
    # Recursive Step: break down and call self
    else:
        return n * factorial(n - 1)
```

---

### How it Works: The Call Stack

Python uses a **call stack** to manage function calls. When a function is called, a new "frame" is pushed onto the stack. When a function returns, its frame is popped off.

For recursion, each recursive call adds a new frame to the stack. The base case stops the process, and the results are returned as the stack unwinds.

**Example: `factorial(3)`**
1. `factorial(3)` is called. Pushed to stack.
2. `factorial(3)` calls `factorial(2)`. Pushed to stack.
3. `factorial(2)` calls `factorial(1)`. Pushed to stack.
4. `factorial(1)` hits the base case and returns `1`. Popped from stack.
5. `factorial(2)` gets `1`, calculates `2 * 1 = 2`, returns `2`. Popped from stack.
6. `factorial(3)` gets `2`, calculates `3 * 2 = 6`, returns `6`. Popped from stack.

**Space Complexity:** Because of the call stack, a recursive function uses space. The space complexity is proportional to the maximum depth of the recursion, which is O(n) for a simple recursion like factorial.

### Pros and Cons

- **Pros:** Can lead to very clean, elegant, and easy-to-read solutions for problems that are naturally recursive (e.g., tree traversals, backtracking).
- **Cons:** Can be less efficient than iterative solutions due to function call overhead. Can lead to stack overflow errors if the recursion is too deep.
