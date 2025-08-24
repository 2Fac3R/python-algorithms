
# Solutions: Exam - Sliding Window

---

### Question 1 (Concept)

What kind of problems are best suited for the Sliding Window technique?

- **Correct Answer:** b) Problems that require finding an optimal or specific **subsequence** (like a subarray or substring).
- **Explanation:** The technique is designed to efficiently analyze contiguous blocks of data.

---

### Question 2 (Pattern Identification)

You are asked to find the "longest substring with at most `k` distinct characters". Since the length of the substring is not fixed, which Sliding Window pattern should you use?

- **Pattern:** Variable-Size Window (or Dynamic Window).

---

### Question 3 (Code Logic)

In a variable-size window, you have two pointers, `start` and `end`. Which pointer is responsible for **expanding** the window, and which is responsible for **shrinking** it when a condition is violated?

- **Expanding Pointer:** `end`
- **Shrinking Pointer:** `start`

---

### Question 4 (Use Case)

To find the "maximum sum of any contiguous subarray of size `k`", you use a fixed-size window. After calculating the sum of the first window, how do you efficiently calculate the sum of the next window in O(1) time?

- **Answer:** You slide the window by **adding** the new element that enters the window (at the `end`) and **subtracting** the element that falls out of the window (at the `start`).

