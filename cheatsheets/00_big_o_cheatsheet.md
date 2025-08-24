
# Cheatsheet: Big O Notation

**Core Concept:** A way to describe how the runtime or space usage of an algorithm scales with the input size `n`.

---

### Common Time Complexities (Best to Worst)

| Notation    | Name         | Example                 | Visual         |
|:------------|:-------------|:------------------------|:---------------|
| **O(1)**    | Constant     | `my_dict['key']`        | `----------`   |
| **O(log n)**| Logarithmic  | Binary Search           | `_______/`     |
| **O(n)**    | Linear       | Single `for` loop       | `_ /`          |
| **O(n log n)**| Log-Linear   | `list.sort()`           | `_/`           |
| **O(n²)**   | Quadratic    | Nested `for` loops      | `J`            |

---

### Key Takeaways

- **Goal:** Aim for the lowest complexity possible.
- **Dominant Term:** In a multi-step algorithm, the slowest step determines the final complexity. `O(n log n) + O(n)` is just `O(n log n)`.
- **Space vs. Time:** Often, you can use more space (e.g., a hash table) to decrease the time complexity. This is a common trade-off.

---

### Space Complexity

| Notation | Name      | Example                               |
|:---------|:----------|:--------------------------------------|
| **O(1)** | Constant  | Algorithm uses a few fixed variables. |
| **O(n)**  | Linear    | Creating a copy or a `set` of a list. |
| **O(n²)** | Quadratic | Creating an `n x n` matrix.           |
