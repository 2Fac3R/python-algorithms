
# Solutions: Exam - Two Pointers

---

### Question 1 (Concept)

What is the primary goal of using the Two Pointers technique?

- **Correct Answer:** b) To reduce the time or space complexity of a brute-force solution, often from O(n²) to O(n).
- **Explanation:** The technique avoids nested loops by intelligently traversing the data structure in a single pass.

---

### Question 2 (Pattern Identification)

You are given a **sorted** array and need to find a pair of elements that sum to a target value. Which Two Pointers pattern is most suitable for this, and where would you initialize the pointers?

- **Pattern:** Converging Pointers (or Opposite Ends).
- **Initialization:** `left` pointer at the **start (index 0)**, `right` pointer at the **end (index len(arr) - 1)**.

---

### Question 3 (Code Logic)

In the "Converging Pointers" pattern (e.g., `left` at start, `right` at end), if the current sum of `arr[left] + arr[right]` is **less than** the target, which pointer should you move to get closer to the target, and in which direction?

- **Pointer to move:** `left`
- **Direction:** To the right (`left += 1`).
- **Explanation:** Since the array is sorted, moving the left pointer to the right will select a larger number, thus increasing the sum.

---

### Question 4 (Use Case)

What is a classic problem that is perfectly solved using the **Fast & Slow** Two Pointers pattern to modify an array in-place?

- **Answer:** Removing duplicates from a sorted array.

