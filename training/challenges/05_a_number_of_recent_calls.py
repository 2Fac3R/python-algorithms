"""
Challenge: Number of Recent Calls

You have a `RecentCounter` class which counts the number of recent requests within a certain time frame.

Implement the `RecentCounter` class:
- `RecentCounter()`: Initializes the counter with zero recent requests.
- `ping(t)`: Adds a new request at time `t` (in milliseconds) and returns the number of requests that has happened in the past 3000 milliseconds (including the new request). Specifically, return the number of requests that have happened in the inclusive range `[t - 3000, t]`.

Technique:
A **Queue** is the ideal data structure for this problem. As new pings arrive, you add their timestamps to the queue. To find the number of recent pings, you just need to remove old timestamps from the front of the queue that are outside the `[t - 3000, t]` window. The size of the queue then gives you the answer.

Instructions:
1. Read the theory on Queues in `training/techniques/05_queues_bfs.md`.
2. Implement the `RecentCounter` class below.
3. Run this file to test your solution.

"""
import collections


class RecentCounter:

    def __init__(self):
        # Your implementation here
        pass

    def ping(self, t: int) -> int:
        # Your implementation here
        pass


# --- Tests ---
def run_tests():
    # Step-by-step test case
    commands = ["RecentCounter", "ping", "ping", "ping", "ping"]
    inputs = [[], [1], [100], [3001], [3002]]
    expected_outputs = [None, 1, 2, 3, 3]

    counter = None
    test_passed = True

    for i in range(len(commands)):
        command = commands[i]
        if command == "RecentCounter":
            counter = RecentCounter()
            print("Test Case 1: `RecentCounter()` -> Initialized")
        else:
            result = counter.ping(inputs[i][0])
            expected = expected_outputs[i]
            if result == expected:
                print(
                    f"Test Case 1: `ping({inputs[i][0]})` -> {result}. PASSED")
            else:
                print(
                    f"Test Case 1: `ping({inputs[i][0]})` -> {result}. FAILED. Expected {expected}")
                test_passed = False

    if test_passed:
        print("\nAll Test Cases Passed!")
    else:
        print("\nSome Test Cases Failed.")


if __name__ == "__main__":
    run_tests()
