
# Exam: Recursion

**Instructions:** Answer the following questions based on the theory document.

---

### Question 1 (Concept)

What are the two essential components of any valid recursive function?

1.  ?
2.  ?

---

### Question 2 (Analysis)

What is the most likely outcome of running a recursive function that is missing a base case?

a) The function will return `None`.
b) The function will run very slowly.
c) The program will crash with a `RecursionError` (stack overflow).
d) The function will return `0`.

---

### Question 3 (Code Output)

What will `my_func(3)` return for the function defined below?

```python
def my_func(n):
    if n <= 0:
        return 0
    return n + my_func(n - 1)
```

- **Answer:** ?

---

### Question 4 (Complexity)

What causes a recursive function to have a space complexity of O(n) in many cases (like factorial or the function in Question 3)?

- **Reason:** ?

