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
    print(solution.twoSum([2, 7, 11, 15], 9))