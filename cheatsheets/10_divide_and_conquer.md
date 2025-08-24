
# Cheatsheet: Divide and Conquer

**Core Concept:** A recursive paradigm that solves a problem by breaking it into smaller, **independent** subproblems, solving them, and combining their results.

---

### The 3 Steps

1.  **Divide:** Split the main problem into subproblems.
    - *Example (Merge Sort):* `mid = len(arr) // 2`, `left = arr[:mid]`, `right = arr[mid:]`

2.  **Conquer:** Solve the subproblems recursively. The recursion stops at a base case (a problem small enough to be solved directly).
    - *Example (Merge Sort):* `sorted_left = sort(left)`, `sorted_right = sort(right)`

3.  **Combine:** Merge the sub-solutions to get the final solution.
    - *Example (Merge Sort):* `return merge(sorted_left, sorted_right)`

---

### General Template

```python
def divide_and_conquer(problem):
    if is_base_case(problem):
        return solve_directly(problem)
    else:
        subproblems = divide(problem)
        sub_solutions = [divide_and_conquer(p) for p in subproblems]
        return combine(sub_solutions)
```

---

### Classic Examples & Complexity

- **Merge Sort:** O(n log n)
- **Quick Sort:** O(n log n) on average, O(n²) in the worst case.
- **Binary Search:** O(log n)
