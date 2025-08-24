
"""
Challenge: Number of 1 Bits

Write a function that takes an unsigned integer and returns the number of '1' bits it has (also known as the Hamming weight).

Example:
Input: n = 11 (binary: 1011)
Output: 3

Technique:
This can be solved with bit manipulation. A common approach is to repeatedly check the last bit of the number and then shift the number to the right. A more clever trick involves using the expression `n & (n - 1)`.
"""

def hammingWeight(n: int) -> int:
    # Your implementation here
    pass

# --- Tests ---
def run_tests():
    test_cases = [
        (11, 3), # 1011
        (128, 1), # 10000000
        (2147483645, 30) # 1111111111111111111111111111101
    ]

    for i, (n, expected) in enumerate(test_cases):
        result = hammingWeight(n)
        if result == expected:
            print(f"Test Case {i + 1}: PASSED")
        else:
            print(f"Test Case {i + 1}: FAILED. Expected {expected}, got {result}")

if __name__ == "__main__":
    run_tests()
