
# Solutions: Exam - Bit Manipulation

---

### Question 1 (Properties)

What is the result of the bitwise expression `x ^ x`, where `x` is any integer?

- **Correct Answer:** b) 0
- **Explanation:** Any number XORed with itself results in zero, as all corresponding bits are the same.

---

### Question 2 (Application)

What is the most common use case for the XOR (`^`) operator in coding challenges involving arrays?

- **Answer:** To find the single unique element in an array where all other elements appear exactly twice.

---

### Question 3 (Code Logic)

How can you efficiently check if a number `num` is **even** using only bitwise operators?

- **Code:** `if (num & 1) == 0:`
- **Explanation:** The expression `num & 1` isolates the least significant bit. This bit is 1 for odd numbers and 0 for even numbers.

---

### Question 4 (Analysis)

What does the expression `x << 3` do to the integer `x`?

- **Answer:** It multiplies `x` by 8 (or 2³).
- **Explanation:** A left shift by `k` positions is equivalent to multiplying by `2^k`.

