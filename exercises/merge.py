from typing import List


def merge(nums1: List[int], m: int, nums2: List[int], n: int) -> List[int]:
    """Merge Sorted Array

    Merge nums1 and nums2 into a single array sorted in non-decreasing order.

    Args:
        nums1 (List[int]): sorted list in non-decreasing order
        m (int): number of elements in nums1
        nums2 (List[int]): sorted list in non-decreasing order
        n (int): number of elements in nums2

    Returns:
        List[int]: a single list sorted in non-decreasing order.

    Tests:
        >>> merge([1, 2, 3, 0, 0, 0], 3, [2, 5, 6], 3)
        [1, 2, 2, 3, 5, 6]
        >>> merge([1], 1, [], 0)
        [1]
        >>> merge([0], 0, [1], 1)
        [1]
    """
    merge = nums1 + nums2
    merge = sorted(list(filter(lambda x: x != 0, merge)))
    return sorted(merge)


if __name__ == '__main__':
    import doctest
    doctest.testmod()
