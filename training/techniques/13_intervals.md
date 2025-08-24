
# Technique: Interval Problems

Interval problems are a common category of questions that involve dealing with ranges, which are typically represented as pairs or lists of two numbers: `[start, end]`.

Examples include meeting schedules, time ranges, or numerical segments on a line.

### The Golden Rule: Sort First!

The single most important strategy for almost all interval problems is to **sort the intervals first**. Usually, you will sort them based on their **start time**.

Sorting creates an ordered structure that makes it much easier to reason about overlaps and merge intervals in a single pass (O(n)) after the initial sort (O(n log n)).

```python
intervals = [[1,3], [8,10], [2,6]]
# Sort by the start time (the first element in each sub-array)
intervals.sort(key = lambda i: i[0])
# Now, intervals is [[1,3], [2,6], [8,10]]
```

---

## The "Merge Intervals" Pattern

This is the most fundamental pattern for interval problems.

**How to Detect an Overlap:**

After sorting, to check if the `current_interval` overlaps with the `previous_interval`, you only need to check one condition:

`current_interval[start] <= previous_interval[end]`

**The Algorithm:**

1.  Sort the intervals by their start time.
2.  Initialize a `merged` list and add the very first interval to it.
3.  Iterate through the rest of the intervals (from the second one onwards).
4.  For each `current_interval`, compare it with the **last interval** in the `merged` list (`last_merged`).
5.  **If they overlap** (`current_interval[start] <= last_merged[end]`):
    -   Update the end of `last_merged` to be the maximum of the two end times: `last_merged[end] = max(last_merged[end], current_interval[end])`.
6.  **If they do not overlap:**
    -   Add the `current_interval` to the `merged` list as a new, separate interval.

After the loop, `merged` will contain the final list of non-overlapping intervals.

**Code Example (Merge Logic):**
```python
# intervals are already sorted
merged = [intervals[0]]
for current in intervals[1:]:
    last_merged = merged[-1]
    # Check for overlap
    if current[0] <= last_merged[1]:
        # Merge
        last_merged[1] = max(last_merged[1], current[1])
    else:
        # No overlap
        merged.append(current)
```
