
from typing import List

"""
Solution for: Generate Parentheses
"""

def generateParenthesis(n: int) -> List[str]:
    """
    This solution uses backtracking. The helper function `backtrack` builds the
    parenthesis string incrementally, keeping track of the number of open and
    close parentheses used so far.
    """
    result = []
    current_string = []

    def backtrack(open_count, close_count):
        # Base Case: If we have used all pairs, we have a valid solution.
        if len(current_string) == 2 * n:
            result.append("".join(current_string))
            return

        # Recursive Step:
        
        # Choice 1: Add an open parenthesis if we can.
        if open_count < n:
            current_string.append("(")
            backtrack(open_count + 1, close_count)
            current_string.pop() # Backtrack

        # Choice 2: Add a close parenthesis if it's valid to do so.
        if close_count < open_count:
            current_string.append(")")
            backtrack(open_count, close_count + 1)
            current_string.pop() # Backtrack

    backtrack(0, 0)
    return result
