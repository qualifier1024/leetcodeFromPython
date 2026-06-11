"""
13. Roman to Integer / 罗马数字转整数 (Easy)

罗马数字包含以下七种字符： I, V, X, L, C, D, M
给定一个罗马数字，将其转换为整数。

Roman numerals are represented by seven different symbols: I, V, X, L, C, D, M.
Given a roman numeral, convert it to an integer.

Example 1:
Input: s = "III"
Output: 3

Example 2:
Input: s = "LVIII"
Output: 58

Example 3:
Input: s = "MCMXCIV"
Output: 1994
"""


class Solution:
    def romanToInt(self, s: str) -> int:
        sni =0
        snm=0
        roma={
            'I':1,
            'V':5,
            'X':10,
            'L':50,
            'C':100,
            'D':500,
            'M':1000
        }
        for i in s[::-1]:
            ni=roma[i]
            if ni>=sni:
                snm+=ni
                sni=ni
            else:
                snm-=ni
        return snm


if __name__ == "__main__":
    solution = Solution()
    print("Example 1:", solution.romanToInt("III"))      # Expected: 3
    print("Example 2:", solution.romanToInt("LVIII"))    # Expected: 58
    print("Example 3:", solution.romanToInt("MCMXCIV"))  # Expected: 1994
