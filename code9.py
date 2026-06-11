"""
9. Palindrome Number / 回文数 (Easy)

给你一个整数 x，如果 x 是一个回文整数，返回 true；否则，返回 false。
回文数是指正序（从左向右）和倒序（从右向左）读都是一样的整数。

Given an integer x, return true if x is a palindrome, and false otherwise.

Example 1:
Input: x = 121
Output: true

Example 2:
Input: x = -121
Output: false

Example 3:
Input: x = 10
Output: false
"""


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
    print("Example 1:", solution.isPalindrome(121))   # Expected: True
    print("Example 2:", solution.isPalindrome(-121))  # Expected: False
    print("Example 3:", solution.isPalindrome(10))    # Expected: False
