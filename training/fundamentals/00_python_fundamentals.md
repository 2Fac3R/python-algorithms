# 00 - Python Fundamentals for Problem Solving

This is a concrete review of the Python features and data structures that are most essential for solving algorithmic challenges.

### 1. Core Data Structures

#### Lists (Dynamic Arrays)
Your most common tool. Use it when you need an ordered collection.
`my_list = [1, 5, 2]`
- **Access:** `my_list[0]` (O(1))
- **Modify:** `my_list[1] = 99` (O(1))
- **Append:** `my_list.append(4)` (Amortized O(1))
- **Pop:** `my_list.pop()` (O(1) from end)
- **Initialization:** `my_list = [0] * 5` # Creates [0, 0, 0, 0, 0]

#### Dictionaries (Hash Maps)
The key to many optimal solutions. Use them for fast lookups (key-value pairs).
`my_dict = {'a': 1}`
- **Access:** `my_dict['a']` (O(1) avg), `my_dict.get('b', 0)` (Safe access)
- **Insert/Update:** `my_dict['b'] = 2` (O(1) avg)
- **Note on Keys:** Dictionary keys must be **hashable** (immutable). Strings, numbers, and tuples can be keys. Lists and other dictionaries cannot.
  - `my_dict[(1, 2)] = 3` (Valid)
  - `my_dict[[1, 2]] = 3` (TypeError!)

#### Sets
Use for storing unique elements and fast membership tests.
`my_set = {1, 2, 3}`
- **Add:** `my_set.add(3)` (Does nothing, already exists)
- **Membership Test:** `if 2 in my_set:` (O(1) avg)

### 2. Mutability vs. Immutability

A key concept that explains how different data types behave.

- **Immutable (Cannot be changed):** Once created, its value cannot be modified. Any "modification" creates a completely new object.
  - **Examples:** `int`, `float`, `str`, `bool`, `tuple`

- **Mutable (Can be changed):** Its value can be modified in-place after creation.
  - **Examples:** `list`, `dict`, `set`

**Why it Matters:**
- Explains why `my_list.sort()` changes the original, but `my_string.lower()` returns a new string.
- Explains why only immutable types (like `tuple`) can be dictionary keys.
- Be careful when passing mutable objects like lists to functions, as the function can modify the original object.

### 3. Essential Built-in Functions

#### `enumerate()`
Use when you need both the index and the value of a list during iteration.
```python
# Instead of this:
for i in range(len(my_list)):
    print(i, my_list[i])

# Do this:
for index, value in enumerate(my_list):
    print(index, value)
```

#### `sorted()` vs. `list.sort()`
- **`sorted(my_list)`:** Returns a **new** sorted list, leaving the original unchanged.
- **`my_list.sort()`:** Sorts the list **in-place** and returns `None`.
```python
# sorted() is great for creating canonical keys for anagrams
key = "".join(sorted("tea")) # key becomes "aet"
```

#### `sum()`, `max()`, `min()`
These are fast, O(n) functions for common calculations on iterables.

### 4. Common String Methods

Essential for cleaning and validating input data.

- **Case Conversion:** `.lower()`, `.upper()`
- **Splitting & Joining:** `"a-b-c".split('-')` (str to list), `"-".join(['a', 'b'])` (list to str)

- **Validation (`is...` methods):**

| Method | Returns `True` if all characters are... | Example |
|:---|:---|:---|
| **`.isalnum()`** | Letters **or** Numbers (Alphanumeric) | `"Python123"` |
| **`.isalpha()`** | Letters only (Alphabetic) | `"Python"` |
| **`.isdigit()`** | Numbers only (Digits) | `"123"` |
| **`.isspace()`** | Whitespace only (e.g. ` ` `\t` `\n`) | `" \t"` |
| **`.islower()`** | Lowercase letters | `"python"` |
| **`.isupper()`** | Uppercase letters | `"PYTHON"` |

### 5. The `collections` Module: Your Superpowers

#### `collections.deque` (Double-Ended Queue)
Use this instead of a `list` for efficient appends and pops from **both ends** (O(1)). Perfect for queues.

#### `collections.defaultdict`
Simplifies code by providing a default value for missing keys. `defaultdict(list)` is great for grouping items.

#### `collections.Counter`
A specialized dictionary for counting hashable objects. `Counter("hello")` -> `{'h':1, 'e':1, 'l':2, 'o':1}`

### 6. Comprehensions

A concise, "Pythonic" way to create collections from iterables.

- **List Comprehension:**
  `squares = [i * i for i in range(5)]`
  `# Result: [0, 1, 4, 9, 16]`

- **Set Comprehension (for unique values):**
  `unique_squares = {i * i for i in [1, 2, 2, 3]}`
  `# Result: {1, 4, 9}`

- **Dictionary Comprehension:**
  `sq_dict = {x: x*x for x in range(3)}`
  `# Result: {0: 0, 1: 1, 2: 4}`

- **Generator Expression (for Tuples):**
  There is no direct tuple comprehension. You use a generator expression inside the `tuple()` constructor.
  `sq_tuple = tuple(i * i for i in range(5))`
  `# Result: (0, 1, 4, 9, 16)`

### 7. Functions and Type Hinting
All challenges use functions and type hints for clarity.
`def has_duplicates(nums: List[int]) -> bool:`

Here are some of the most common types used in the challenges. Most require an import from the `typing` module.

| Type Hint | Represents | Import From |
|:---|:---|:---|
| `int`, `str`, `bool` | Standard primitive types. | (built-in) |
| `List[int]` | A list of integers. | `from typing import List` |
| `Dict[str, int]` | A dictionary with string keys and integer values. | `from typing import Dict` |
| `Set[str]` | A set of strings. | `from typing import Set` |
| `Tuple[int, ...]` | A tuple containing integers. | `from typing import Tuple` |
| `Optional[str]` | A value that can be a string or `None`. | `from typing import Optional` |
| `Any` | Can be of any type. Used as an escape hatch. | `from typing import Any` |

**Note on Python Versions:** In Python 3.9 and newer, you can use the built-in types directly for type hinting (e.g., `list[int]` instead of `List[int]`). This guide uses the capitalized `typing` module format (e.g., `List`, `Dict`) because it is backwards-compatible with Python 3.6-3.8, ensuring the code works for more users.

### 8. Error Handling (try...except)

Instead of letting your program crash from a potential error, you can handle it gracefully.

- **`try`:** The code that might cause an error goes here.
- **`except`:** If an error occurs, this code is executed. Catch specific errors for robust code.
- **`else`:** (Optional) Runs only if the `try` block completes **without** any errors.
- **`finally`:** (Optional) Runs **no matter what**. Useful for cleanup.

**Clearer Example:**
```python
def get_value_safely(my_dict: dict, key: any):
    print(f"--- Attempting to access key: '{key}' ---")
    try:
        value = my_dict[key]
    except KeyError:
        print(f"Error: Key '{key}' not found.")
        return None
    else:
        print("Success! Value found.")
        return value
    finally:
        print("Cleanup: Operation finished.\n")

get_value_safely({"a": 1}, "a")
get_value_safely({"a": 1}, "b")
```

**Common Built-in Exceptions:**

| Exception | When it Occurs | Example |
|:---|:---|:---|
| `IndexError` | List index is out of range. | `my_list[99]` |
| `KeyError` | Dictionary key is not found. | `my_dict['key']` |
| `ValueError` | Right type, but invalid value. | `int('abc')` |
| `TypeError` | Wrong type for an operation. | `'hello' + 5` |

### 9. Naming Conventions (PEP 8 & Best Practices)

Writing clean code includes using clear, conventional names.

- **General Style:**
  - `snake_case_for_variables_and_functions`
  - `UPPER_SNAKE_CASE_for_constants`

- **Variables:**
  - **Be Descriptive:** `left_pointer` is better than `lp`.
  - **Use Plurals for Collections:** Name lists or sets with plural nouns (e.g., `numbers`, `words`).

- **Functions:**
  - **Use Verbs:** Name functions with verbs that describe what they do (e.g., `calculate_sum`, `get_username`).
  - **For Boolean Functions (Return `True`/`False`):** Name them like questions.

| Prefix | Meaning | Example |
|:---|:---|:---|
| `is_` | Checks a state or quality. | `is_empty`, `is_valid` |
| `has_` | Checks for a property or item. | `has_duplicates`, `has_key` |
| `can_` | Checks for an ability. | `can_construct`, `can_edit` |

### 10. Class Basics (OOP)

Some challenges require you to understand or use classes. A class is a blueprint for creating objects.

```python
# All challenges with Trees use this class definition
class TreeNode:
    # The __init__ method is the constructor, called when you create an object.
    # `self` refers to the specific object instance being created.
    def __init__(self, val=0, left=None, right=None):
        # Attributes are variables that belong to the object.
        self.val = val
        self.left = left
        self.right = right

# Creating an instance (object) of the class
root_node = TreeNode(10)
root_node.left = TreeNode(5)
```
- **`class TreeNode:`**: Defines the blueprint.
- **`__init__`**: The special constructor method.
- **`self`**: Represents the object instance itself.
- **`self.val`**: An attribute (a variable) belonging to the object.
