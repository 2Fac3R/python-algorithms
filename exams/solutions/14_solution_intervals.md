
# Solutions: Exam - Interval Problems

---

### Question 1 (Concept)

What is the single most important first step for solving almost any interval-based problem?

- **Answer:** Sorting the intervals, usually by their start time.

---

### Question 2 (Analysis)

Assuming you have two intervals that are already sorted by their start times, `A = [start_A, end_A]` and `B = [start_B, end_B]`. What is the simple condition to check if they overlap?

- **Condition:** `start_B <= end_A`

---

### Question 3 (Application)

If you determine that `A = [3, 9]` and `B = [5, 12]` overlap, what is the resulting merged interval?

- **Answer:** `[3, 12]`
- **Explanation:** The new interval is `[min(start_A, start_B), max(end_A, end_B)]` which is `[min(3,5), max(9,12)]`.

---

### Question 4 (Algorithm Logic)

When iterating through a sorted list of intervals to merge them, you compare the `current_interval` with which other interval to check for an overlap?

- **Correct Answer:** c) The last interval that was added to your `merged` results list.

