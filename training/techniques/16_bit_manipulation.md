
# Technique: Bit Manipulation

**Bit Manipulation** is the act of algorithmically manipulating bits or other pieces of data shorter than a word. This technique involves using bitwise operators to work directly with the binary representation of numbers. For a certain class of problems, it can lead to solutions that are extremely fast and memory-efficient.

### Why is it important?

While less common than array or string problems, bit manipulation questions are used to test a candidate's deeper understanding of how data is represented at a low level. A clever bitwise solution can often reduce a complex problem to a few lines of elegant, efficient code.

---

## Key Bitwise Operators in Python

| Operator | Name | Example (a=5, b=3) `0101 & 0011` | Description |
|:---|:---|:---|:---|
| **`&`** | AND | `a & b` -> `0001` (1) | Sets a bit to 1 only if both corresponding bits are 1. |
| **`|`** | OR | `a | b` -> `0111` (7) | Sets a bit to 1 if at least one of the corresponding bits is 1. |
| **`^`** | XOR | `a ^ b` -> `0110` (6) | Sets a bit to 1 only if the corresponding bits are different. |
| **`~`** | NOT | `~a` -> `-6` | Inverts all the bits. (Uses two's complement for negative numbers). |
| **`<<`** | Left Shift | `a << 1` -> `1010` (10) | Shifts bits to the left, padding with zeros. Equivalent to multiplying by 2. |
| **`>>`** | Right Shift | `a >> 1` -> `0010` (2) | Shifts bits to the right, discarding the rightmost bits. Equivalent to integer division by 2. |

---

## Common Tricks and Properties

-   **XOR (`^`) is the most useful operator in interviews.**
    -   `x ^ x = 0` (Any number XORed with itself is zero).
    -   `x ^ 0 = x` (Any number XORed with zero is itself).
    -   `x ^ y ^ y = x` (XOR is reversible. This is the key to finding a unique number in a list of duplicates).
    -   It is commutative and associative: `a ^ b = b ^ a` and `(a ^ b) ^ c = a ^ (b ^ c)`.

-   **AND (`&`) is great for checking bits.**
    -   `x & 1`: Returns 1 if `x` is odd, 0 if `x` is even. A fast way to check parity.
    -   `x & (x - 1)`: This expression **clears the least significant bit** (the rightmost '1'). This is a clever trick used to count the number of set bits.
    -   `x & (1 << k)`: Checks if the k-th bit of `x` is set.

-   **Shifts (`<<`, `>>`) for powers of 2.**
    -   `1 << k`: Creates a number with only the k-th bit set. This is useful for creating bitmasks.
