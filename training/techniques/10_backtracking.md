
# Algorithmic Paradigm: Backtracking

**Backtracking** is an algorithmic technique for solving problems recursively by trying to build a solution incrementally. It involves exploring all possible paths to a solution and abandoning ("backtracking" from) a path as soon as it is determined that it cannot possibly lead to a valid solution.

It is a refined form of brute-force search, where the algorithm intelligently prunes branches of the search space that are guaranteed not to contain a solution.

### The Core Idea: "Choose, Explore, Un-choose"

Every backtracking solution can be thought of as a recursive function that follows a simple three-step mantra:

1.  **Choose:** Make a choice. This could be adding a number to a temporary list, placing a queen on a chessboard, or adding a character to a string.
2.  **Explore:** After making a choice, recursively call the function to explore the subsequent decisions that follow from this choice.
3.  **Un-choose (Backtrack):** When the recursive call returns, you **undo** the choice you made in step 1. This is the most critical part of backtracking. It allows you to return to the previous state and explore a *different* path. For example, if you added a number to a list, you would now remove it.

### General Template

Most backtracking problems can be solved with a helper function that follows this structure:

```python
def find_solutions(input_data):
    result = []

    def backtrack(current_state, other_params...):
        # Base Case: Check if the current state is a valid solution
        if is_a_solution(current_state):
            result.append(create_copy_of(current_state))
            return

        # Iterate through all possible choices from the current state
        for choice in get_possible_choices(current_state):
            
            # 1. Choose
            add_choice_to_state(choice, current_state)

            # 2. Explore
            backtrack(current_state, ...)

            # 3. Un-choose (This is the backtrack step!)
            remove_choice_from_state(choice, current_state)

    backtrack(initial_state, ...)
    return result
```

### Common Use Cases

Backtracking is ideal for problems that ask for "all possible" solutions or involve permutations, combinations, and subsets.

-   Generating all permutations of a set.
-   Generating all subsets of a set (the power set).
-   Solving puzzles like Sudoku or N-Queens.
-   Combination Sum problems.
