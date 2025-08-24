
"""
Challenge: Min Stack

Design a stack that supports push, pop, top, and retrieving the minimum element in constant time.

Implement the `MinStack` class:
- `__init__()` initializes the stack object.
- `push(val: int)` pushes the element `val` onto the stack.
- `pop()` removes the element on the top of the stack.
- `top()` gets the top element of the stack.
- `getMin()` retrieves the minimum element in the stack.

Each function should operate in **O(1)** time.

Technique:
The key to this problem is how to keep track of the minimum element in O(1) time. A standard stack doesn't do this. The common solution is to use a second stack (a `min_stack`) that stores the minimum value seen at each stage.
"""

class MinStack:

    def __init__(self):
        # Your implementation here
        pass

    def push(self, val: int) -> None:
        # Your implementation here
        pass

    def pop(self) -> None:
        # Your implementation here
        pass

    def top(self) -> int:
        # Your implementation here
        pass

    def getMin(self) -> int:
        # Your implementation here
        pass

# --- Tests ---
def run_tests():
    print("Running MinStack tests...")
    minStack = MinStack()
    minStack.push(-2)
    minStack.push(0)
    minStack.push(-3)
    
    # Test 1: getMin() should be -3
    min_val = minStack.getMin()
    print(f"Test 1: getMin() -> Expected -3, Got {min_val}" if min_val == -3 else f"Test 1: FAILED. Expected -3, Got {min_val}")

    # Test 2: pop()
    minStack.pop()
    
    # Test 3: top() should be 0
    top_val = minStack.top()
    print(f"Test 3: top() -> Expected 0, Got {top_val}" if top_val == 0 else f"Test 3: FAILED. Expected 0, Got {top_val}")

    # Test 4: getMin() should be -2
    min_val = minStack.getMin()
    print(f"Test 4: getMin() -> Expected -2, Got {min_val}" if min_val == -2 else f"Test 4: FAILED. Expected -2, Got {min_val}")
    print("Tests finished.")

if __name__ == "__main__":
    run_tests()
