
# Cheatsheet: Binary Search

**Core Concept:** An O(log n) algorithm for finding a target in a **SORTED** array by repeatedly dividing the search space in half.

**When to Use:**
- **MUST** be a sorted collection.
- Searching for an element or an insertion position.
- Can be adapted to find min/max values that satisfy a condition in a monotonic search space.

---

### Implementation

```python
left, right = 0, len(arr) - 1
target = ...

while left <= right:
    mid = left + (right - left) // 2

    if arr[mid] == target:
        # Found it!
        return mid
    elif arr[mid] < target:
        # Search in the right half
        left = mid + 1
    else:
        # Search in the left half
        right = mid - 1

# Target not found
return -1
```

---

### Visual Logic

`arr = [2, 5, 7, 8, 11, 12]`, `target = 12`

1. `L=0, R=5, M=2` (`arr[2]` is 7, too small) -> `L` becomes `3`
2. `L=3, R=5, M=4` (`arr[4]` is 11, too small) -> `L` becomes `5`
3. `L=5, R=5, M=5` (`arr[5]` is 12, **match!**) -> `return 5`

**Complexity:** `Time: O(log n)`, `Space: O(1)`
