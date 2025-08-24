
# Solutions: Exam - Big O Notation

---

### Question 1 (Multiple Choice)

An algorithm has O(1) time complexity. If the input data size doubles, how does the runtime change?

- **Correct Answer:** b) It remains exactly the same.
- **Explanation:** O(1) means constant time. The runtime is independent of the input size `n`.

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

- **Time Complexity:** O(n²)
- **Space Complexity:** O(n²)
- **Reasoning:**
    - **Time:** The code has a nested loop. The outer loop runs `n` times, and for each of a those iterations, the inner loop also runs `n` times. This results in `n * n = n²` operations.
    - **Space:** The `pairs` list stores a new tuple for every combination of `item1` and `item2`. It will hold `n * n = n²` tuples in total, so the space required grows quadratically with the input size.

---

### Question 3 (Matching)

Match the time complexity with its most common practical example from the theory guide.

- `O(log n)` -> **D) `Binary Search`**
- `O(n)` -> **C) `for item in my_list:`**
- `O(1)` -> **A) `my_dict['key']`**
- `O(n log n)` -> **B) `my_list.sort()`**

---

### Question 4 (Short Answer)

Why is an algorithm with O(n) complexity generally preferred over one with O(n²)?

- **Answer:** An algorithm with O(n) complexity scales linearly with the input size, while an O(n²) algorithm scales quadratically. This means that for large inputs, the O(n²) algorithm will become dramatically and unmanageably slower than the O(n) one. It is far more efficient.

