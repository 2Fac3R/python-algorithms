
# Solutions: Exam - Stacks (LIFO)

---

### Question 1 (Concept)

A stack follows the LIFO principle. What does LIFO stand for?

- **Answer:** Last-In, First-Out.

---

### Question 2 (Application)

What is the most classic use case for a stack, as mentioned in the theory guide, which involves validating correctly ordered pairs of symbols?

- **Answer:** Validating parentheses (e.g., `()[]{}`).

---

### Question 3 (Code Logic)

In Python, you can use a `list` as a stack. Which list methods would you use for the following stack operations?

- **Push (add an item):** `my_list.append()`
- **Pop (remove an item):** `my_list.pop()`

---

### Question 4 (Algorithm Logic)

To implement a "Min Stack" that returns the minimum element in O(1) time, what common technique or auxiliary data structure is used alongside the main stack?

- **Answer:** A second, auxiliary stack (often called a `min_stack`). This second stack keeps track of the minimum value of the main stack at every point in time.

