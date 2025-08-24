
# Cheatsheet: Bit Manipulation

**Core Concept:** Using bitwise operators (`&`, `|`, `^`, `~`, `<<`, `>>`) for highly efficient, low-level calculations on the binary representation of numbers.

---

### Core Operators & Tricks

| Operator | Name | Example | Result / Key Use Case |
|:---|:---|:---|:---|
| **`&`** | AND | `num & 1` | Checks if `num` is odd (1) or even (0). |
| **`|`** | OR | `num | (1<<k)` | Sets the k-th bit of `num` to 1. |
| **`^`** | XOR | `x ^ y ^ y` | Returns `x`. Used to find the single unique number. |
| **`<< k`** | Left Shift | `x << 1` | Multiplies `x` by 2. `1 << k` creates a bitmask. |
| **`>> k`** | Right Shift| `x >> 1` | Integer divides `x` by 2. |

---

### The Most Common Tricks

1.  **Find the Single Unique Number in Duplicates**
    -   **Technique:** XOR all elements together. The duplicates cancel to 0, leaving the unique number.
    -   **Code:** `reduce(lambda a, b: a ^ b, nums)`

2.  **Count the Number of 1-bits (Hamming Weight)**
    -   **Technique:** In a loop, repeatedly apply `n = n & (n - 1)`. This expression clears the rightmost '1' bit. The number of loops is the answer.
    -   **Code:** `while n: n &= (n-1); count += 1`

3.  **Check if the k-th bit is set**
    -   **Technique:** Left shift 1 by `k` positions to create a mask, then AND it with the number.
    -   **Code:** `if num & (1 << k): ...`
