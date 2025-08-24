
# Technique: Sliding Window

The **Sliding Window** technique is a powerful method for solving problems that involve finding an optimal or specific subsequence (like a subarray or substring) within a larger sequence. The core idea is to maintain a "window" (a sub-list or sub-string) and "slide" it over the data, adjusting its size dynamically.

This approach is significantly more efficient than a brute-force method that would check every possible subsequence. It typically reduces the time complexity from O(n²) or O(n*k) to O(n).

## Common Patterns

### 1. Fixed-Size Window

This is the simpler pattern. The window size is fixed, and you just slide it from the beginning to the end of the sequence.

- **Initialize:** Calculate the value for the first window of size `k`.
- **Slide:** In each step, slide the window one position to the right by **adding** the new element at the end and **subtracting** the element that is now out of the window from the beginning.

**When to use it:**
- Problems where you need to find something in a contiguous subarray of a **fixed size `k`**.

**Example Problems:**
- Maximum sum of any contiguous subarray of size `k`.
- Find all anagrams of a string `p` in a string `s`.

**Code Example (Max Sum Subarray):**
```python
# O(1) operation to slide the window
window_sum = window_sum + new_element - old_element
```

### 2. Variable-Size Window (Dynamic Window)

This is a more advanced and common pattern. The window size grows and shrinks based on certain conditions.

- **Pointers:** Use two pointers, `start` and `end`, to define the current window.
- **Expand:** Move the `end` pointer to the right to grow the window.
- **Shrink:** When the window no longer meets the problem's constraints (e.g., contains duplicate characters, sum exceeds a target), move the `start` pointer to the right to shrink the window until it's valid again.

**When to use it:**
- Problems where you need to find the **longest, shortest, or best** subarray/substring that satisfies a certain property.

**Example Problems:**
- Longest substring without repeating characters.
- Smallest subarray with a sum greater than or equal to a target value.
- Longest substring with at most `k` distinct characters.
