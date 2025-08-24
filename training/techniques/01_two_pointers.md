
# Technique: Two Pointers

The **Two Pointers** technique is an extremely common and effective strategy used to optimize algorithms that operate on sequences like arrays or strings. It involves using two integer pointers (indices) that move through the data structure, either towards each other, away from each other, or in the same direction.

This technique often helps reduce the time complexity of a brute-force solution from O(n²) to O(n) and/or the space complexity from O(n) to O(1).

## Common Patterns

There are two main patterns for the two-pointers technique:

### 1. Converging Pointers (Opposite Ends)

This is the most frequent pattern. You initialize one pointer at the beginning of the sequence and the other at the end. They move towards each other until they meet or cross.

- **`left` starts at `0`**
- **`right` starts at `len(sequence) - 1`**
- **Loop Condition:** `while left < right:`

**When to use it:**
This pattern is ideal for problems where you need to find a pair of elements that satisfy a certain condition and the sequence is **sorted** (or can be processed symmetrically).

**Example Problems:**
- Checking if a string is a palindrome.
- Finding two numbers in a sorted array that sum up to a target value.

**Code Example (Two Sum II):**
```python
left, right = 0, len(sorted_arr) - 1
target = 10

while left < right:
    current_sum = sorted_arr[left] + sorted_arr[right]
    if current_sum == target:
        # Found pair
        return [left, right]
    elif current_sum < target:
        left += 1
    else:
        right -= 1
```

### 2. Same-Direction Pointers (Fast and Slow)

In this pattern, both pointers start at or near the beginning of the sequence but move at different speeds. One pointer (the "fast" one) iterates through the elements, while the other (the "slow" one) only moves when a certain condition is met.

- **`slow` starts at `0`**
- **`fast` starts at `0` or `1`**
- **Loop Condition:** The `fast` pointer usually iterates through the entire sequence (`for fast in range(len(sequence))`).

**When to use it:**
This is useful for problems involving processing elements and making a decision based on a "window" or a subsequence, such as removing duplicates or finding cycles.

**Example Problems:**
- Removing duplicates from a sorted array in-place.
- Detecting a cycle in a linked list (Floyd's Tortoise and Hare algorithm).
