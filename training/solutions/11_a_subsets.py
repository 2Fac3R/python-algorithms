
from typing import List

"""
Solution for: Subsets
"""

def subsets(nums: List[int]) -> List[List[int]]:
    """
    This solution uses a backtracking approach with a helper function (DFS).

    The `backtrack` function builds a subset incrementally. The `start` parameter
    is used to ensure that we only consider elements at or after the current position,
    which prevents generating duplicate subsets (e.g., we generate [1,2] but not [2,1]).
    """
    result = []
    current_subset = []

    def backtrack(start: int):
        # First, add a copy of the current subset. This represents one valid subset.
        result.append(list(current_subset))

        # Explore further options by adding subsequent numbers.
        for i in range(start, len(nums)):
            # 1. Choose: Add the number to our current subset.
            current_subset.append(nums[i])

            # 2. Explore: Recurse with the next starting position.
            backtrack(i + 1)

            # 3. Un-choose (Backtrack): Remove the number to explore other paths.
            current_subset.pop()

    backtrack(0)
    return result
