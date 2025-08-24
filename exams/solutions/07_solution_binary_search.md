
# Solutions: Exam - Binary Search

---

### Question 1 (Prerequisite)

What is the single most important condition that an array must satisfy before you can apply Binary Search to it?

- **Answer:** The array must be **sorted**.

---

### Question 2 (Concept)

Binary Search is a "divide and conquer" algorithm. What does this mean in the context of the algorithm?

- **Answer:** It means that in each step, the algorithm divides the search space (the part of the array it's looking at) in half, effectively conquering or eliminating half of the remaining elements from consideration.

---

### Question 3 (Code Logic)

In an iterative binary search with pointers `left` and `right`, you calculate `mid`. If the `target` value is **greater than** the element at `array[mid]`, how must you adjust your pointers to continue the search?

- **Action:** `left = mid + 1`
- **Explanation:** Since the array is sorted, if the target is greater than the middle element, it must be in the right half of the current search space.

---

### Question 4 (Complexity)

What is the time complexity of Binary Search and why is it so efficient?

- **Time Complexity:** O(log n)
- **Reason for Efficiency:** It is efficient because it doesn't need to check every element. By halving the search space in every step, the number of comparisons grows very slowly even for very large lists.

