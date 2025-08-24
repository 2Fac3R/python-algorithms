
from typing import List
import functools

"""
Solution for: Single Number
"""

def singleNumber(nums: List[int]) -> int:
    """
    This solution leverages the properties of the XOR bitwise operator.

    - `x ^ x = 0` (A number XORed with itself is zero)
    - `x ^ 0 = x` (A number XORed with zero is itself)

    If we XOR all the numbers in the list together, every number that appears twice
    will cancel itself out (e.g., `... ^ 2 ^ ... ^ 2 ^ ...` becomes `... ^ 0 ^ ...`).
    The only number remaining at the end of the cumulative XOR operation will be the
    one that appeared only once.

    Example: [4, 1, 2, 1, 2]
    - 0 ^ 4 = 4
    - 4 ^ 1 = 5
    - 5 ^ 2 = 7
    - 7 ^ 1 = 6 (since 1 was already in the mix, its bits are flipped back)
    - 6 ^ 2 = 4 (since 2 was already in the mix, its bits are flipped back)
    Result: 4
    """
    # Initialize with 0, because x ^ 0 = x
    result = 0
    for num in nums:
        result ^= num
    return result

    # A more concise way using functools.reduce:
    # return functools.reduce(lambda a, b: a ^ b, nums)
