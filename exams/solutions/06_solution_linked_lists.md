
# Solutions: Exam - Linked List Manipulation

---

### Question 1 (Concept)

What is the primary advantage of a linked list over an array, and what is its primary disadvantage?

- **Advantage:** Efficient insertions and deletions at any point in the list (O(1) if you have the node, O(n) to find it).
- **Disadvantage:** No direct access to elements by index. Accessing the `i`-th element takes O(i) time.

---

### Question 2 (Pattern Identification)

Which two-pointer pattern is used to detect a cycle in a linked list, and what is it often called?

- **Pattern:** Fast & Slow Pointers.
- **Name:** Floyd's Tortoise and Hare Algorithm.

---

### Question 3 (Code Logic)

When reversing a linked list iteratively, you use `prev` and `current` pointers. After the line `current.next = prev`, what must you do to advance the pointers correctly?

- **Correct Answer:** c) `prev = current` then `current = a_stored_next_node`
- **Explanation:** You must first store `current.next` in a temporary variable *before* you reverse the pointer. Then, you can advance `prev` to `current` and `current` to the stored next node.

---

### Question 4 (Application)

What is a "dummy head node" (or sentinel node) and why is it useful when merging two sorted linked lists?

- **Answer:** It is a placeholder node that comes before the actual head of the list you are building. It is useful because it simplifies the code by providing a guaranteed starting point, which eliminates the need to write special edge case logic for inserting into an empty list.

