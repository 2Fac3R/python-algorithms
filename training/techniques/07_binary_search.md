
# Technique: Binary Search

**Binary Search** is a highly efficient searching algorithm that works on **sorted** arrays. It follows a "divide and conquer" strategy to find the position of a target value within the array.

Its main advantage is its time complexity of **O(log n)**, which is a massive improvement over the O(n) complexity of a simple linear search, especially for large datasets.

## The Algorithm

1.  **Prerequisite:** The array or sequence **must be sorted**.
2.  **Pointers:** Start with two pointers, `left` and `right`, at the beginning and end of the array, respectively.
3.  **Loop:** Continue as long as `left <= right`.
    a.  **Midpoint:** Calculate the middle index: `mid = left + (right - left) // 2`. (This formula is used to prevent potential integer overflow in other languages, and is good practice in Python too).
    b.  **Compare:** Compare the element at the `mid` index with the `target` value.
        i.  **Match:** If `array[mid] == target`, the element has been found. Return `mid`.
        ii. **Target is smaller:** If `target < array[mid]`, the target must be in the left half of the current search space. So, discard the right half by setting `right = mid - 1`.
        iii. **Target is larger:** If `target > array[mid]`, the target must be in the right half. Discard the left half by setting `left = mid + 1`.
4.  **Not Found:** If the loop finishes without finding the target, it means the target is not in the array. Return -1 or an appropriate indicator.

## Why is it so important?

Binary search is a fundamental algorithm. It appears not only in its basic form but also as a building block for more complex problems. The core idea of repeatedly halving a search space can be applied to many problems, not just searching in arrays. For example, it can be used to find the minimum value that satisfies a condition or the square root of a number.

**Variations:**
- Finding the first or last occurrence of an element.
- Finding the smallest element greater than the target (Ceiling).
- Finding the largest element smaller than the target (Floor).
- Searching in a rotated sorted array.
