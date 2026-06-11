"""
5. Longest Palindromic Substring / 最长回文子串 (Medium)

给你一个字符串 s，找到 s 中最长的回文子串。

Given a string s, return the longest palindromic substring in s.

Example 1:
Input: s = "babad"
Output: "bab" (or "aba")

Example 2:
Input: s = "cbbd"
Output: "bb"

Example 3:
Input: s = "a"
Output: "a"
"""


class Solution(object):
    def longestPalindrome(self, s):
        """
        :type s: str
        :rtype: str
        """
        re = [0, ]
        te = []

        def hui(ls, rs):

            n = rs - ls + 1
            if n > re[-1]:
                re.append(rs - ls + 1)
                te.append((ls, rs))
            if ls == 0 or rs == len(s) - 1:
                return
            if s[ls - 1] == s[rs + 1]:
                hui(ls - 1, rs + 1)
            return

        lz = 0
        while lz < (len(s) - 1):

            hui(lz, lz)
            if s[lz + 1] == s[lz]:
                hui(lz, lz + 1)
            lz = lz + 1
        if len(s) == 1:
            return s

        return s[te[-1][0]:te[-1][1] + 1]


if __name__ == "__main__":
    solution = Solution()
    print("Example 1:", solution.longestPalindrome("babad"))  # Expected: "bab" or "aba"
    print("Example 2:", solution.longestPalindrome("cbbd"))   # Expected: "bb"
    print("Example 3:", solution.longestPalindrome("a"))      # Expected: "a"
