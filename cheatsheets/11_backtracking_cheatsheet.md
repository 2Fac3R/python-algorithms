
# Cheatsheet: Backtracking

**Core Concept:** A recursive technique to find all possible solutions by incrementally building candidates and abandoning a path ("backtracking") as soon as it's determined to be invalid.

---

### The 3-Step Mantra

For every possible choice from the current state:

1.  **Choose:** Make the choice (e.g., add an element to a list).
2.  **Explore:** Recurse with the new state to see where this choice leads.
3.  **Un-choose:** Undo the choice (e.g., remove the element from the list). This is the critical backtrack step that allows you to explore other paths.

---

### General Template

```python
result = []

def backtrack(current_state, ...):
    if is_solution(current_state):
        result.append(copy(current_state))
        return

    for choice in get_possible_choices():
        # 1. Choose
        add_to_state(choice)

        # 2. Explore
        backtrack(new_state, ...)

        # 3. Un-choose
        remove_from_state(choice)
```

---

### Common Problems Solved with Backtracking

- **Subsets:** For each element, choose to include it or not.
- **Permutations:** For each position, choose from the remaining available numbers.
- **Combinations:** Similar to subsets, but with a fixed size.
- **Generate Parentheses:** Choose to add '(' or ')' based on constraints.
- **Puzzle Solvers:** Sudoku, N-Queens, Word Search.
