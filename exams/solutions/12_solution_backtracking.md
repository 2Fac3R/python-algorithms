
# Solutions: Exam - Backtracking

---

### Question 1 (Concept)

What is the three-step pattern or "mantra" that is central to all backtracking algorithms?

1.  **Choose**
2.  **Explore**
3.  **Un-choose** (or Backtrack)

---

### Question 2 (Analysis)

In a backtracking algorithm, what is the purpose of the "un-choose" or backtrack step?

- **Correct Answer:** b) To undo a choice so that other paths can be explored from the previous state.
- **Explanation:** The un-choose step is what allows the algorithm to "go back" and try a different decision from a previous branching point.

---

### Question 3 (Application)

Which of the following problems is a classic candidate for a backtracking solution?

- **Correct Answer:** c) Generating all possible subsets of a set.
- **Explanation:** Problems that ask for "all possible" combinations, permutations, or subsets are prime candidates for backtracking.

---

### Question 4 (Code Logic)

In the "Generate Parentheses" problem for `n=3`, you have a partial string `"(()"`. You have used 2 open and 1 close parenthesis. According to the rules, what is your next valid move?

- **Correct Answer:** c) You can add either an open or a close parenthesis.
- **Explanation:**
    - You can add an open parenthesis because `open_count (2) < n (3)`.
    - You can add a close parenthesis because `close_count (1) < open_count (2)`.

