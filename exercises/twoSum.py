"""
Two Sum
Given an array of integers nums and an integer target, return indices of the two numbers such that they add up to target.
You may assume that each input would have exactly one solution, and you may not use the same element twice.

Example 1:

Input: nums = [2,7,11,15], target = 9
Output: [0,1]
Explanation: Because nums[0] + nums[1] == 9, we return [0, 1].

Example 2:

Input: nums = [3,2,4], target = 6
Output: [1,2]

Example 3:

Input: nums = [3,3], target = 6
Output: [0,1]
"""


def twoSum(nums: list, target: int) -> list:
    for i in range(len(nums) - 1):
        sum = nums[i] + nums[i+1]
        if sum == target:
            return [i, i+1]
    return []


if __name__ == '__main__':
    nums: list = [2, 7, 11, 15]
    target: int = 9

    print(twoSum(nums, target))
