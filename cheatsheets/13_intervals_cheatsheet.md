
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

**Logic:** Sort intervals by start time. Iterate and compare the current interval with the end of the last interval in the result list. If it overlaps, merge them by updating the end time; otherwise, add it as a new interval.

**Implementation Snippet:**
```python
intervals.sort(key=lambda i: i[0])
merged = [intervals[0]]
for current in intervals[1:]:
    last_merged = merged[-1]
    if current[0] <= last_merged[1]:
        last_merged[1] = max(last_merged[1], current[1])
    else:
        merged.append(current)
```
