
# Exam: Python Fundamentals for Problem Solving

**Instructions:** Answer the following questions based on the theory document.

---

### Question 1 (Code Output)

What will the following Python code print?

```python
from collections import deque

my_list = [10, 20, 30, 40]
q = deque(my_list)

q.append(50)
q.popleft()
q.pop()

print(q)
```

---

### Question 2 (Fill in the Blank)

To safely get a value from a dictionary without causing a `KeyError` if the key does not exist, you should use the `.______('key', default_value)` method.

---

### Question 3 (Code Analysis)

What is the primary advantage of using a `set` over a `list` to check if an item exists in a collection of unique items? 

- **Answer:** ?
- **Reasoning (in terms of Big O):** ?

---

### Question 4 (Short Answer)

Briefly explain what `collections.defaultdict(int)` does and why it is useful.

