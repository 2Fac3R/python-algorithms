
# Cheatsheet: Interval Problems

**Core Concept:** A common problem type involving ranges `[start, end]`. The solution almost always involves sorting and then iterating.

---

### The Golden Rule: SORT FIRST!

For nearly all interval problems, the first step is to sort the intervals by their **start time**.

```python
# Sort list of lists by the first element of each inner list
intervals.sort(key = lambda i: i[0])
```

---

### The Merge Pattern

This pattern is used to merge overlapping intervals into a set of non-overlapping ones.

**Logic:**
1.  Sort the intervals.
2.  Initialize `merged = [intervals[0]]`.
3.  Loop through the rest of the `intervals`:
    -   Get the `last_merged = merged[-1]`.
    -   Get the `current_interval`.
    -   **Check for overlap:** `if current_interval[0] <= last_merged[1]:`
        -   **If Overlap:** Update the end of the last interval: `last_merged[1] = max(last_merged[1], current_interval[1])`.
    -   **Else (No Overlap):**
        -   Add the current interval to the results: `merged.append(current_interval)`.

**Overall Complexity:** O(n log n) time (dominated by the sort), O(n) space (for the result).
