# 00 - Big O Notation: A Practical Summary

Understanding Big O notation is the single most important prerequisite for analyzing algorithms. It's not about exact timing; it's about understanding how an algorithm's performance **scales** as the input size (`n`) grows.

--- 

### O(1) - Constant Time

The algorithm takes the same amount of time, regardless of the input size.

**Practical Examples:**
- Accessing an element in an array or list by its index.
- Getting a value from a hash map (dictionary) by its key.
- Pushing or popping from a stack.

```python
# Accessing a dictionary key is O(1)
def get_first_price(prices: dict) -> int:
    # It doesn't matter if the dict has 1 or 1,000,000 items,
    # this lookup takes roughly the same time.
    return prices["apple"]
```

---

### O(log n) - Logarithmic Time

The algorithm's time complexity grows logarithmically. This means the time it takes to run halves with each step. It's incredibly efficient for large datasets.

**Practical Example:**
- **Binary Search** on a sorted array.

```python
# The core loop of Binary Search is O(log n)
def binary_search(sorted_list: list, target: int):
    left, right = 0, len(sorted_list) - 1
    while left <= right:
        mid = (left + right) // 2
        if sorted_list[mid] == target:
            return mid
        elif sorted_list[mid] < target:
            left = mid + 1
        else:
            right = mid - 1
    # With each iteration, we cut the search space in half.
```

---

### O(n) - Linear Time

The runtime grows linearly with the input size. If the input size doubles, the runtime roughly doubles.

**Practical Examples:**
- Iterating through all elements of a list or array once.
- Finding an item in an unsorted list.

```python
# A single loop over a list is O(n)
def find_max(numbers: list) -> int:
    max_val = numbers[0]
    # The loop runs n times, where n is len(numbers).
    for num in numbers:
        if num > max_val:
            max_val = num
    return max_val
```

---

### O(n log n) - Log-Linear Time

This is the hallmark of efficient "divide and conquer" algorithms. It's significantly better than O(n²) but not as fast as O(n).

**Intuitive Explanation:**
Imagine you have to sort a deck of 8 cards.
1.  **The `log n` part (Divide):** You split the deck in half (4 cards), then split those halves (2 cards), then again (1 card). It takes you 3 splits to get down to individual cards. This "splitting" action is the `log n` part. `log₂(8) = 3`.
2.  **The `n` part (Conquer):** Now you have to merge them back together in sorted order. To merge two piles, you have to look at every card (`n` operations). You do this for each level of splitting.

So, you perform `n` work `log n` times, leading to **O(n log n)**.

**Practical Example: Checking for Duplicates (Alternative Method)**
A very common pattern is to sort the data first to make processing easier. This example finds duplicates in a list.

```python
# Problem: Check if a list contains any duplicate numbers.
# This approach is O(n log n) because of the sorting step.

def has_duplicates_sorted(numbers: list) -> bool:
    # Step 1: Sort the list. This is the dominant step.
    # Complexity: O(n log n)
    numbers.sort()

    # Step 2: Iterate through the sorted list and check adjacent elements.
    # Complexity: O(n)
    for i in range(len(numbers) - 1):
        if numbers[i] == numbers[i+1]:
            return True # Found a duplicate
    return False

# The total complexity is O(n log n) + O(n), which simplifies to O(n log n)
# because we only care about the fastest-growing term.
```
This is a great example of how sorting can be a powerful first step in solving a problem, often setting the overall complexity of the algorithm.

---

### O(n²) - Quadratic Time

The runtime grows quadratically with the input size. This is common in algorithms with nested loops over the same data. It becomes very slow, very quickly.

**Practical Example:**
- A nested loop to compare every element with every other element.
- Bubble Sort, Insertion Sort.

```python
# A nested loop is the classic O(n²) example.
def find_duplicates(numbers: list) -> bool:
    # For each number...
    for i in range(len(numbers)):
        # ...compare it to every other number.
        for j in range(len(numbers)):
            if i != j and numbers[i] == numbers[j]:
                return True # Found a duplicate
    return False
```

---

### Space Complexity

Big O also describes memory usage. It's crucial for environments with limited memory and for understanding the full cost of an algorithm.

**O(1) Space: Constant Space**
You use a fixed amount of memory, regardless of the input size. This is the most memory-efficient.

```python
# This function uses O(1) space.
# It only uses a few variables (sum_val, num), no matter how large the list is.
def get_sum(numbers: list) -> int:
    sum_val = 0
    for num in numbers:
        sum_val += num
    return sum_val
```

**O(n) Space: Linear Space**
Your memory usage grows linearly with the input size.

```python
# This function uses O(n) space because it creates a new list
# whose size depends on the input list's size.
def create_copy(numbers: list) -> list:
    # The new_list grows to the same size as the input 'numbers'.
    new_list = []
    for num in numbers:
        new_list.append(num)
    return new_list

# Another O(n) example: creating a set from a list.
# In the worst case (all unique elements), the set will have n items.
def get_unique_items(numbers: list) -> set:
    return set(numbers)
```

**O(n²) Space: Quadratic Space**
Memory usage grows quadratically with the input size. This is rare and often undesirable.

```python
# This function uses O(n²) space because it creates an n-by-n matrix.
def create_matrix(n: int) -> list[list[int]]:
    matrix = []
    for i in range(n):
        row = [0] * n
        matrix.append(row)
    return matrix
# If n=10, you store 10*10=100 elements. If n=100, you store 100*100=10,000 elements.

# The `create_pairs` function from the exam is another example,
# as it stores n*n pairs in a list.
```

---

### Visual Comparison of Common Complexities

This text-based graph illustrates how the number of operations (runtime) grows for each complexity class as the input size (`n`) increases. The steeper the curve, the less efficient the algorithm is with large inputs.

```text
^ Operations
|
|                                                     O(n²) (terrible)
|                                                   . 
|                                                 .  
|                                               .    
|                                             .      
|                                           .        
|                                         .          
|                                       / O(n log n) (good)
|                                     /              
|                                   /                
|                                 /                  
|                               /                    
|                             / O(n) (fair/good)
|                           /
|                         /
|                       /
|_____________________/___________ O(log n) (excellent)
|--------------------------------- O(1) (perfect/ideal)
+-----------------------------------------------------> Input Size (n)
```