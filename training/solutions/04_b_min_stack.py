
"""
Solution for: Min Stack
"""

class MinStack:
    """
    This solution uses two stacks to achieve the O(1) time complexity for all operations.

    - `self.stack`: This is the main stack that stores all the elements pushed.
    - `self.min_stack`: This auxiliary stack keeps track of the minimums. The top of `min_stack`
      is always the minimum element of the entire `self.stack`.
    """

    def __init__(self):
        self.stack = []
        self.min_stack = []

    def push(self, val: int) -> None:
        """
        When pushing a new value:
        1. Push the value onto the main stack.
        2. For the min_stack, compare the new value with the current minimum (which is the top
           of min_stack). Push the smaller of the two onto min_stack.
        3. If min_stack is empty, just push the new value.
        """
        self.stack.append(val)
        current_min = self.min_stack[-1] if self.min_stack else val
        self.min_stack.append(min(val, current_min))

    def pop(self) -> None:
        """
        To maintain synchronization, when we pop from the main stack, we must also pop
        from the min_stack. This ensures the top of min_stack always corresponds to the
        current state of the main stack.
        """
        if self.stack:
            self.stack.pop()
            self.min_stack.pop()

    def top(self) -> int:
        """
        Returns the top of the main stack.
        """
        if self.stack:
            return self.stack[-1]

    def getMin(self) -> int:
        """
        The minimum element of the entire stack is always at the top of our min_stack.
        This is an O(1) operation.
        """
        if self.min_stack:
            return self.min_stack[-1]
