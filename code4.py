"3"


class Solution:
    def findMedianSortedArrays(self, nums1, nums2):
        nums3 = nums1 + nums2
        nums3.sort()
        n = len(nums3)
        if n % 2 == 0:
            a = n / 2
            b = a - 1
            cen = (nums3[a] + nums3[b]) / 2.0
            return cen
        else:
            i = (n - 1) / 2
            num = nums3[i]
            return num
