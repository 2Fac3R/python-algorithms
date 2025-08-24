
# Solutions: Exam - Recursion

---

### Question 1 (Concept)

What are the two essential components of any valid recursive function?

1.  **Base Case:** The condition that stops the recursion.
2.  **Recursive Step:** The part where the function calls itself with a smaller/simpler input.

---

### Question 2 (Analysis)

What is the most likely outcome of running a recursive function that is missing a base case?

- **Correct Answer:** c) The program will crash with a `RecursionError` (stack overflow).
- **Explanation:** Without a base case, the function will call itself indefinitely, adding a new frame to the call stack with each call until the stack's memory limit is exceeded.

---

### Question 3 (Code Output)

What will `my_func(3)` return for the function defined below?

```python
def my_func(n):
    if n <= 0:
        return 0
    return n + my_func(n - 1)
```

- **Answer:** 6
- **Explanation:** The calls are `3 + my_func(2)` -> `3 + (2 + my_func(1))` -> `3 + (2 + (1 + my_func(0)))` -> `3 + (2 + (1 + 0))` = 6.

---

### Question 4 (Complexity)

What causes a recursive function to have a space complexity of O(n) in many cases (like factorial or the function in Question 3)?

- **Reason:** The **call stack**. Each recursive call adds a new frame to the stack until the base case is reached. The maximum depth of this stack is proportional to `n`.

