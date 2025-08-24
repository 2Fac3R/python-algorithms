
from typing import List

"""
Solution for: Coin Change
"""

def coinChange(coins: List[int], amount: int) -> int:
    """
    This solution uses Dynamic Programming with a bottom-up (Tabulation) approach.

    1. We create a `dp` array of size `amount + 1`. `dp[i]` will store the minimum
       number of coins needed to make the amount `i`.
    2. We initialize all values in `dp` to a value that represents infinity (e.g., `amount + 1`)
       to signify that these amounts are not yet reachable. `dp[0]` is initialized to 0,
       as 0 coins are needed to make an amount of 0.
    3. We iterate through each amount `a` from 1 to `amount`.
    4. For each amount `a`, we iterate through each `coin` denomination.
    5. If a `coin` is less than or equal to the current `amount` `a`, it means we can
       potentially use this coin. The number of coins would be `1` (for the current coin)
       plus the minimum coins needed for the remaining amount, which is `dp[a - coin]`.
    6. We update `dp[a]` to be the minimum of its current value and `1 + dp[a - coin]`.
    7. After filling the table, `dp[amount]` will hold the answer. If its value is still
       our infinity-like value, it means the amount was unreachable.
    """
    # Initialize dp array with a value larger than any possible amount
    dp = [amount + 1] * (amount + 1)
    dp[0] = 0

    for a in range(1, amount + 1):
        for coin in coins:
            if a - coin >= 0:
                dp[a] = min(dp[a], 1 + dp[a - coin])

    if dp[amount] == amount + 1:
        return -1 # Amount cannot be made up
    else:
        return dp[amount]
