class Solution(object):
    def isPalindrome(self, x):
        """
        :type x: int
        :rtype: bool
        """
        s = str(x)
        return True if s == s[::-1] else False


if __name__ == "__main__":
    solution = Solution()
    print(solution.isPalindrome(121))