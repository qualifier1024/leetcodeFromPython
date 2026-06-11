"""
16. 3Sum Closest / 最接近的三数之和 (Medium)

给你一个长度为 n 的整数数组 nums 和一个目标值 target。请你从 nums 中选出三个整数，
使它们的和与 target 最接近。返回这三个数的和。
假定每组输入恰好只存在一个解。

Given an integer array nums of length n and an integer target, find three integers in nums
such that the sum is closest to target. Return the sum of the three integers.
You may assume that each input would have exactly one solution.

Example 1:
Input: nums = [-1,2,1,-4], target = 1
Output: 2

Example 2:
Input: nums = [0,0,0], target = 1
Output: 0
"""


from typing import List


class Solution:
    def threeSumClosest(self, nums: List[int], target: int) -> int:
        nums.sort()
        closest = sum(nums[:3])
        n = len(nums)
        for i in range(n - 2):
            left, right = i + 1, n - 1
            while left < right:
                total = nums[i] + nums[left] + nums[right]
                if abs(total - target) < abs(closest - target):
                    closest = total
                if total < target:
                    left += 1
                elif total > target:
                    right -= 1
                else:
                    return total
        return closest


if __name__ == "__main__":
    solution = Solution()
    print(solution.threeSumClosest([-1,2,1,-4], 1))