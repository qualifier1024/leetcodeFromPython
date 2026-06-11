"""
4. Median of Two Sorted Arrays / 寻找两个正序数组的中位数 (Hard)

给定两个大小分别为 m 和 n 的正序（从小到大）数组 nums1 和 nums2。请你找出并返回这两个正序数组的中位数。

Given two sorted arrays nums1 and nums2 of size m and n respectively, return the median of the two sorted arrays.

Example 1:
Input: nums1 = [1,3], nums2 = [2]
Output: 2.0

Example 2:
Input: nums1 = [1,2], nums2 = [3,4]
Output: 2.5

Example 3:
Input: nums1 = [0,0], nums2 = [0,0]
Output: 0.0
"""


class Solution:
    def findMedianSortedArrays(self, nums1, nums2):
        nums3 = nums1 + nums2
        nums3.sort()
        n = len(nums3)
        if n % 2 == 0:
            a = n // 2
            b = a - 1
            cen = (nums3[a] + nums3[b]) / 2.0
            return cen
        else:
            i = (n - 1) // 2
            num = nums3[i]
            return num


if __name__ == "__main__":
    solution = Solution()
    print("Example 1:", solution.findMedianSortedArrays([1, 3], [2]))     # Expected: 2.0
    print("Example 2:", solution.findMedianSortedArrays([1, 2], [3, 4]))  # Expected: 2.5
    print("Example 3:", solution.findMedianSortedArrays([0, 0], [0, 0]))  # Expected: 0.0
