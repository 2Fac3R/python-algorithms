from typing import List


def two_sum(nums: List[int], target: int) -> List[int]:
    """Two Sum

    Args:
        nums (List[int]): a list of integers nums
        target (int): an integer target

    Returns:
        List[int]: indices of the two numbers such that they add up to target.

    Tests:
        >>> two_sum([2, 7, 11, 15], 9)
        [0, 1]
        >>> two_sum([3, 2, 4], 6)
        [1, 2]
        >>> two_sum([3, 3], 6)
        [0, 1]
        >>> two_sum([2, 7, 11, 15], 9)
        [0, 1]
        >>> two_sum([15, 2, 11, 7], 13)
        [1, 2]
        >>> two_sum([2, 7, 11, 15], 17)
        [0, 3]
        >>> two_sum([7, 15, 11, 2], 18)
        [0, 2]
        >>> two_sum([2, 7, 11, 15], 26)
        [2, 3]
        >>> two_sum([2, 7, 11, 15], 8)
        []
        >>> two_sum([3 * i for i in range(10)], 19)
        []
    """
    # Brute Force - Time: O(n^2) Space: O(1)
    # for i in range(len(nums)):
    #     for j in range(i + 1, len(nums)):
    #         # if nums[j] == target - nums[i]:
    #         if nums[i] + nums[j] == target:
    #             return [i, j]

    # Hash Table - Time: O(n) Space: O(n)
    # hashmap = {}
    # for i in range(len(nums)):
    #     hashmap[nums[i]] = i
    # for i in range(len(nums)):
    #     complement = target - nums[i]
    #     if complement in hashmap and hashmap[complement] != i:
    #         return [i, hashmap[complement]]

    # One-pass Hash Table - Time: O(n) Space: O(n)
    hashmap = {}
    for i in range(len(nums)):
        complement = target - nums[i]
        if complement in hashmap:
            return [hashmap[complement], i]
        hashmap[nums[i]] = i

    return []


if __name__ == '__main__':
    import doctest
    doctest.testmod()
