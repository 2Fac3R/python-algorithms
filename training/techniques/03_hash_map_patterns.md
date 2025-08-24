
# Technique: Hash Tables (Python Dictionaries)

A **Hash Table** is a data structure that implements an associative array abstract data type, a structure that can map keys to values. In Python, the built-in `dict` type is a highly optimized implementation of a hash table.

Hash tables are a cornerstone of algorithm design and are frequently the key to an optimal solution in coding interviews. They excel at trading a bit of memory (space complexity) for a significant improvement in speed (time complexity).

## Core Properties

- **Key-Value Pairs:** They store data as pairs of keys and values.
- **Fast Lookups:** The primary advantage is the speed of operations. On average, insertion, deletion, and lookup (retrieval) of a value by its key are **O(1)** operations.
- **Unordered (Historically):** In older versions of Python (before 3.7), dictionaries were unordered. Since Python 3.7, they maintain insertion order, but you should not rely on this for algorithmic logic unless the problem specifies it.

## Why are they so useful in interviews?

Many brute-force solutions have a time complexity of O(n²) because they involve nested loops to find pairs or check for properties among all elements. A hash table can often eliminate the inner loop.

**Common Use Case: The "Lookup" or "Complement" Pattern**

Instead of iterating through a list to find an element, you can pre-process the list into a hash table. This allows you to check for the existence of an element (or its "complement") in O(1) time.

**Example: The "Two Sum" Problem**

- **Problem:** Find two numbers in a list that add up to a target `T`.
- **Brute-force (O(n²)):** For each number `x`, loop through the rest of the list to see if `T - x` exists.
- **Hash Table (O(n)):** For each number `x`, check if its complement `T - x` is already in the hash table. If it is, you've found a pair. If not, add `x` and its index to the table and move to the next number.

**Code Example (Two Sum):**
```python
num_map = {}
for i, num in enumerate(nums):
    complement = target - num
    if complement in num_map:
        return [num_map[complement], i]
    num_map[num] = i
```

**Other Common Applications:**
- **Counting Frequencies:** Use the element as the key and its frequency as the value (e.g., `counts[char] = counts.get(char, 0) + 1`).
- **Caching/Memoization:** Store the results of expensive computations to avoid recalculating them.
- **Grouping:** Group items with a common property (e.g., grouping anagrams by their sorted-string representation).
