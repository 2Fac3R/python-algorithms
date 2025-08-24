
# Cheatsheet: Sliding Window

**Core Concept:** Maintain a "window" (sub-array/sub-string) and slide it through the data to efficiently find optimal subsequences in O(n) time.

**When to Use:**
- Finding the max/min sum of a subarray of size `k`.
- Finding the longest/shortest substring that satisfies a condition.
- Problems involving contiguous arrays/strings.

---

### Key Patterns

| Pattern | Window Size | Core Logic | Visual |
|:---|:---|:---|:---|
| **Fixed Size** | Stays constant (`k`) | Add new element, subtract old element. | `[L...R] ->` |
| **Variable Size** | Grows & Shrinks | Expand with `R`, shrink with `L` when a condition is broken. | `[L..R] ->`<br>`[L.R] ->` |

---

### Implementation Snippets

**Fixed Window (e.g., Max Sum Subarray of size k):**
```python
# First, sum the initial window
window_sum = sum(arr[:k])
max_sum = window_sum
# Then, slide
for i in range(k, len(arr)):
    window_sum += arr[i] - arr[i - k]
    max_sum = max(max_sum, window_sum)
```

**Variable Window (e.g., Longest Substring w/o repeats):**
```python
# Use a set or dict to track items in window
while end < len(s):
    # Expand window
    # While condition broken:
        # Shrink window
```

**Complexity:** `Time: O(n)`, `Space: O(k)` or `O(1)`
