"""
14. Longest Common Prefix / 最长公共前缀 (Easy)

编写一个函数来查找字符串数组中的最长公共前缀。
如果不存在公共前缀，返回空字符串 ""。

Write a function to find the longest common prefix string amongst an array of strings.
If there is no common prefix, return an empty string "".

Example 1:
Input: strs = ["flower","flow","flight"]
Output: "fl"

Example 2:
Input: strs = ["dog","racecar","car"]
Output: ""

Example 3:
Input: strs = ["a"]
Output: "a"
"""


from typing import List


def longestCommonPrefix(self, strs: List[str]) -> str:
    ans = ''
    for i in list(zip(*strs)):
        if len(set(i)) == 1:
            ans += i[0]
        else:
            break
    return ans


class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        ans = ''
        for i in list(zip(*strs)):
            if len(set(i)) == 1:
                ans += i[0]
            else:
                break
        return ans


if __name__ == "__main__":
    solution = Solution()
    print("Example 1:", solution.longestCommonPrefix(["flower","flow","flight"]))  # Expected: "fl"
    print("Example 2:", solution.longestCommonPrefix(["dog","racecar","car"]))     # Expected: ""
    print("Example 3:", solution.longestCommonPrefix(["a"]))                       # Expected: "a"
