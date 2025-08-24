
# Exam: Big O Notation

**Instructions:** Answer the following questions based on the theory document.

---

### Question 1 (Multiple Choice)

An algorithm has O(1) time complexity. If the input data size doubles, how does the runtime change?

a) It also doubles.
b) It remains exactly the same.
c) It increases by a small amount.
d) It is cut in half.

---

### Question 2 (Code Analysis)

Analyze the time and space complexity of the following Python function. Explain your reasoning.

```python
def create_pairs(my_list: list) -> list:
    pairs = []
    for item1 in my_list:
        for item2 in my_list:
            pairs.append((item1, item2))
    return pairs
```

- **Time Complexity:** ?
- **Space Complexity:** ?
- **Reasoning:** ?

---

### Question 3 (Matching)

Match the time complexity with its most common practical example from the theory guide.

| Complexity  | Example                  |
|-------------|--------------------------|
| `O(log n)`  | A) `my_dict['key']`      |
| `O(n)`      | B) `my_list.sort()`      |
| `O(1)`      | C) `for item in my_list:`|
| `O(n log n)`| D) `Binary Search`       |

---

### Question 4 (Short Answer)

Why is an algorithm with O(n) complexity generally preferred over one with O(n²)?

