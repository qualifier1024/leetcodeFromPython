"""
10. Regular Expression Matching / 正则表达式匹配 (Hard)

给你一个字符串 s 和一个字符规律 p，请你来实现一个支持 '.' 和 '*' 的正则表达式匹配。
'.' 匹配任意单个字符
'*' 匹配零个或多个前面的那一个元素

Given an input string s and a pattern p, implement regular expression matching with support for '.' and '*'.
'.' Matches any single character.
'*' Matches zero or more of the preceding element.

Example 1:
Input: s = "aa", p = "a"
Output: false

Example 2:
Input: s = "aa", p = "a*"
Output: true

Example 3:
Input: s = "ab", p = ".*"
Output: true
"""


class Solution(object):
    def isMatch(self, s, p):
        """
        :type s: str
        :type p: str
        :rtype: bool
        """
        los, t_end, tes = '*', [], 0
        for i in list(p):
            if i == '*':
                if los == '*':
                    return False
                else:
                    t_end += [tes, tes]
            elif los != '*':
                tes += 1
                t_end += [tes]
            los = i
        if p[-1] != '*':
            t_end += [tes + 1]

        def isTrue(o_s, o_p):
            if o_p == '.' or o_p == o_s:
                return True
            return False

        g_act = [[len(s) - 1, len(p) - 1]]
        for act in g_act:
            [si, pi] = act
            if si == -1 and (pi == -1 or t_end[pi] == 0):
                return True
            elif si > -1 and pi > -1:
                if p[pi] == '*' and pi:
                    cp = p[pi - 1]
                    csi = si
                    while csi != -1 and isTrue(s[csi], cp):
                        g_act.append([csi, pi - 2])
                        csi -= 1
                    g_act.append([csi, pi - 2])
                elif isTrue(s[si], p[pi]):
                    g_act.append([si - 1, pi - 1])
        return False


if __name__ == "__main__":
    solution = Solution()
    print("Example 1:", solution.isMatch("aa", "a"))   # Expected: False
    print("Example 2:", solution.isMatch("aa", "a*"))  # Expected: True
    print("Example 3:", solution.isMatch("ab", ".*"))  # Expected: True
