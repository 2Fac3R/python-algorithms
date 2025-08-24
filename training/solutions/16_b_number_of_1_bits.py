
"""
Solution for: Number of 1 Bits
"""

def hammingWeight(n: int) -> int:
    """
    This solution uses a clever bit manipulation trick.

    The expression `n & (n - 1)` has the property of clearing the least significant
    (the rightmost) '1' bit of a number.

    Example: n = 11 (1011)
    - n - 1 = 10 (1010)
    - n & (n - 1) = 1011 & 1010 = 1010 (which is 10)
      The rightmost '1' was cleared.

    By repeatedly applying this operation in a loop until `n` becomes 0, we can count
    how many times we were able to clear a '1' bit. This count is our answer.
    This method is often faster than checking each bit one by one, especially for
    sparse numbers (numbers with few '1's).
    """
    count = 0
    while n > 0:
        # This operation clears the least significant bit
        n = n & (n - 1)
        count += 1
    return count

# Alternative, simpler solution:
# def hammingWeight_simple(n: int) -> int:
#     count = 0
#     while n > 0:
#         # Check if the last bit is 1
#         if n & 1:
#             count += 1
#         # Right shift to check the next bit
#         n = n >> 1
#     return count
