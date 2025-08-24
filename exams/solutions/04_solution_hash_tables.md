
# Solutions: Exam - Hash Tables (Dictionaries)

---

### Question 1 (Concept)

What is the primary advantage of using a hash table, and what is the average time complexity for lookups, insertions, and deletions?

- **Advantage:** Fast lookups (speed).
- **Time Complexity:** O(1) on average.

---

### Question 2 (Use Case)

In the "Two Sum" problem, you are looking for two numbers that add up to a target `T`. If your current number is `x`, what is the "complement" you search for in the hash table?

- **Complement:** `T - x`

---

### Question 3 (Application)

How can a hash table be used to group a list of words by anagrams? What would you use as the **key** in the hash table?

- **Key:** A sorted version of the word. All anagrams will produce the same key when sorted.

---

### Question 4 (Code Logic)

Why is it often better to use `my_dict.get(key, default_value)` instead of `my_dict[key]` when you are not sure if a key exists?

- **Reason:** `my_dict[key]` will raise a `KeyError` if the key is not found, potentially crashing the program. `my_dict.get(key, default_value)` will safely return the `default_value` (e.g., `None` or `0`) instead.

