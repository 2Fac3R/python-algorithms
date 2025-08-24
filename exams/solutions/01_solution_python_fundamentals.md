
# Solutions: Exam - Python Fundamentals for Problem Solving

---

### Question 1 (Code Output)

What will the following Python code print?

```python
from collections import deque

my_list = [10, 20, 30, 40]
q = deque(my_list) # q is deque([10, 20, 30, 40])

q.append(50)       # q is deque([10, 20, 30, 40, 50])
q.popleft()        # q is deque([20, 30, 40, 50])
q.pop()            # q is deque([20, 30, 40])

print(q)
```

- **Output:** `deque([20, 30, 40])`

---

### Question 2 (Fill in the Blank)

To safely get a value from a dictionary without causing a `KeyError` if the key does not exist, you should use the `.get('key', default_value)` method.

- **Answer:** `get`

---

### Question 3 (Code Analysis)

What is the primary advantage of using a `set` over a `list` to check if an item exists in a collection of unique items? 

- **Answer:** Speed / Performance.
- **Reasoning (in terms of Big O):** Checking for membership with `item in my_set` is an **O(1)** operation on average for a set. For a list, `item in my_list` is an **O(n)** operation because Python may have to scan the entire list.

---

### Question 4 (Short Answer)

Briefly explain what `collections.defaultdict(int)` does and why it is useful.

- **Answer:** It creates a dictionary-like object. When you try to access or modify a key that doesn't exist, it automatically creates the key and assigns it a default value by calling the factory provided (`int()` in this case, which returns `0`).
- **Usefulness:** It simplifies code for counting or grouping because you don't need to write extra `if key not in my_dict:` checks before updating a value.

