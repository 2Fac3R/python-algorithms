
"""
Solution for: Number of Recent Calls
"""
import collections

class RecentCounter:
    """
    This solution uses a queue (specifically, `collections.deque`) to store the
    timestamps of the pings.

    `__init__`:
    - We initialize an empty `deque` to store the timestamps of requests.

    `ping(t)`:
    1. **Enqueue:** We add the new timestamp `t` to the right end of our queue.
       This maintains the order of requests.
    2. **Dequeue:** We check the front of the queue. As long as the timestamp at the
       front is older than our time window (i.e., less than `t - 3000`), we
       remove it from the left end of the queue. We repeat this until the
       timestamp at the front is within the valid time window.
    3. **Return Size:** After removing all the old timestamps, the remaining
       timestamps in the queue are all within the `[t - 3000, t]` range.
       The size of the queue is therefore our answer.
    """

    def __init__(self):
        self.requests = collections.deque()

    def ping(self, t: int) -> int:
        # Add the new request timestamp to the queue
        self.requests.append(t)

        # Remove timestamps from the front of the queue that are outside the time window
        while self.requests[0] < t - 3000:
            self.requests.popleft()

        # The size of the queue is the number of recent requests
        return len(self.requests)
