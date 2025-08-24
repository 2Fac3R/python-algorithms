
# Cheatsheet: Hash Tables (Dictionaries)

**Core Concept:** Use key-value pairs for O(1) average time complexity on lookups, insertions, and deletions. It's a massive speed-up for many problems.

**When to Use:**
- **Counting:** Tracking frequencies of items.
- **Grouping:** Grouping items by a certain property (e.g., anagrams).
- **Fast Lookups:** Checking for existence or finding the "complement" in two-sum type problems.

---

### Common Use Cases

| Use Case | Key | Value | Example |
|:---|:---|:---|:---|
| **Counting** | The item itself | Its frequency count | `counts[char] += 1` |
| **Two Sum** | The number | Its index | `num_map[num] = i` |
| **Group Anagrams** | The sorted string | List of anagrams | `groups[sorted_s].append(s)` |

---

### Essential Methods

- **`my_dict[key]`**: Access. Raises `KeyError` if key not found.
- **`my_dict.get(key, default)`**: Safe access. Returns `default` if key not found.
- **`key in my_dict`**: Membership test. Fast and Pythonic.
- **`my_dict.items()`**: Iterate over `(key, value)` pairs.

**Complexity:** `Time: O(1)` (average), `Space: O(n)` (to store `n` items)
