"""
1. Two Sum / 两数之和 (Easy)

给定一个整数数组 nums 和一个整数目标值 target，请你在该数组中找出和为目标值 target 的那两个整数，并返回它们的数组下标。
你可以假设每种输入只会对应一个答案，并且你不能使用两次相同的元素。
你可以按任意顺序返回答案。

Given an array of integers nums and an integer target, return indices of the two numbers such that they add up to target.
You may assume that each input would have exactly one solution, and you may not use the same element twice.
You can return the answer in any order.

Example 1:
Input: nums = [2,7,11,15], target = 9
Output: [0,1]

Example 2:
Input: nums = [3,2,4], target = 6
Output: [1,2]

Example 3:
Input: nums = [3,3], target = 6
Output: [0,1]
"""


class Solution(object):
    def twoSum(self, nums, target):
        d = {}
        j = 0
        for i in nums:
            a = target - i
            if a in d:
                return [d[a], j]
            else:
                d[i] = j
            j += 1
        return []


if __name__ == "__main__":
    solution = Solution()
    print("Example 1:", solution.twoSum([2, 7, 11, 15], 9))   # Expected: [0, 1]
    print("Example 2:", solution.twoSum([3, 2, 4], 6))         # Expected: [1, 2]
    print("Example 3:", solution.twoSum([3, 3], 6))            # Expected: [0, 1]
