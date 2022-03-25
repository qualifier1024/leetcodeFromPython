"1"


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
