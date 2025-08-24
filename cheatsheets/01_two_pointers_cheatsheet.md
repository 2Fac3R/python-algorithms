
# Cheatsheet: Two Pointers

**Core Concept:** Use two indices to traverse a sequence in a single pass, avoiding O(n²) complexity.

**When to Use:**
- On **sorted** arrays to find pairs.
- To check for palindromes.
- To remove duplicates from a sorted array.

---

### Key Patterns

| Pattern | Initialization | Core Logic | Visual |
|:---|:---|:---|:---|
| **Converging** | `L=0`, `R=len-1` | `while L < R:`<br>Move `L` or `R` inward based on a condition. | `L -> ... <- R` |
| **Fast & Slow** | `slow=0`, `fast=0` | `for fast in range...`<br>Move `slow` only when a condition is met. | `S,F -> ...` |

---

### Implementation Snippets

**Converging (e.g., Two Sum on sorted array):**
```python
left, right = 0, len(arr) - 1
while left < right:
    current_sum = arr[left] + arr[right]
    if current_sum == target:
        return [left, right]
    elif current_sum < target:
        left += 1
    else:
        right -= 1
```

**Fast & Slow (e.g., Remove Duplicates from sorted array):**
```python
slow = 0
for fast in range(1, len(nums)):
    if nums[fast] != nums[slow]:
        slow += 1
        nums[slow] = nums[fast]
return slow + 1
```

**Complexity:** `Time: O(n)`, `Space: O(1)`
