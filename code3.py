"""
3. Longest Substring Without Repeating Characters / 无重复字符的最长子串 (Medium)

给定一个字符串 s，请你找出其中不含有重复字符的最长子串的长度。

Given a string s, find the length of the longest substring without repeating characters.

Example 1:
Input: s = "abcabcbb"
Output: 3

Example 2:
Input: s = "bbbbb"
Output: 1

Example 3:
Input: s = "pwwkew"
Output: 3
"""


class Solution(object):
    def lengthOfLongestSubstring(self, s):
        if not s: return 0
        left = 0
        lookup = set()
        n = len(s)
        max_len = 0
        cur_len = 0
        for i in range(n):
            cur_len += 1
            while s[i] in lookup:
                lookup.remove(s[left])
                left += 1
                cur_len -= 1
            if cur_len > max_len:
                max_len = cur_len
            lookup.add(s[i])
        return max_len


if __name__ == "__main__":
    solution = Solution()
    print("Example 1:", solution.lengthOfLongestSubstring("abcabcbb"))  # Expected: 3
    print("Example 2:", solution.lengthOfLongestSubstring("bbbbb"))    # Expected: 1
    print("Example 3:", solution.lengthOfLongestSubstring("pwwkew"))   # Expected: 3
