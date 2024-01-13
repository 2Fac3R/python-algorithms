from typing import List


def merge(nums1: List[int], nums2: List[int]) -> List[int]:
    """Merge Sorted Array

    Merge nums1 and nums2 into a single array sorted in non-decreasing order.

    Args:
        nums1 (List[int]): sorted list in non-decreasing order
        nums2 (List[int]): sorted list in non-decreasing order

    Returns:
        List[int]: a single list sorted in non-decreasing order.

    Tests:
        >>> merge([1, 2, 3, 0, 0, 0], [2, 5, 6])
        [1, 2, 2, 3, 5, 6]
        >>> merge([1], [])
        [1]
        >>> merge([0], [1])
        [1]
    """
    merge: List[int] = nums1 + nums2
    # sorts and removes zeros
    # merge = sorted(list(filter(lambda x: x != 0, merge)))
    merge = sorted([x for x in merge if x != 0])
    return merge


if __name__ == '__main__':
    from doctest import testmod
    testmod()
