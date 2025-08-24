# Algorithmic Paradigm: Divide and Conquer

**Divide and Conquer (D&C)** is a powerful algorithmic paradigm for solving complex problems. The strategy involves systematically breaking a problem into smaller, more manageable subproblems of the same type, solving them, and then combining their solutions to solve the original problem.

This process is typically implemented using recursion.

### The Three Steps of Divide and Conquer

Every D&C algorithm follows three core steps:

1.  **Divide:** The problem is broken down into several smaller, independent subproblems. For example, an array is divided into two halves.

2.  **Conquer:** The subproblems are solved by making recursive calls. If a subproblem is small enough (the base case), it is solved directly.

3.  **Combine:** The solutions to the subproblems are combined to create the solution for the original problem. This step is often the most complex part of the algorithm (e.g., the `merge` step in Merge Sort).

### Visualization: Merge Sort

Merge Sort is the quintessential example of a Divide and Conquer algorithm.

```text
Original Array: [3, 1, 4, 5, 2, 6]

1. DIVIDE
           [3, 1, 4]     [5, 2, 6]
          /         \   /         \
      [3]  [1, 4]   [5]  [2, 6]
           /    \       /    \
         [1]   [4]    [2]   [6]

2. CONQUER (Base Case)
   The single-element arrays are already solved (sorted).

3. COMBINE (Merge)
         [1, 4]       [2, 6]
           \    /
          [1, 3, 4]     [2, 5, 6]
                   \
                 [1, 2, 3, 4, 5, 6]
```

### D&C vs. Dynamic Programming

Both paradigms break problems down, but there is a key difference:

-   **Divide and Conquer:** Deals with **independent** subproblems. The solution for one subproblem is not needed to solve another (e.g., sorting the left half of an array is independent of sorting the right half).
-   **Dynamic Programming:** Deals with **overlapping** subproblems. The same subproblem is solved multiple times, so the results are cached (memoized) to avoid re-computation.

### Common Examples

-   **Merge Sort**
-   **Quick Sort**
-   **Binary Search**

