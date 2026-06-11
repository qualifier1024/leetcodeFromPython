"""
12. Integer to Roman / 整数转罗马数字 (Medium)

罗马数字包含以下七种字符： I, V, X, L, C, D, M
给定一个整数，将其转换为罗马数字。

Roman numerals are represented by seven different symbols: I, V, X, L, C, D, M.
Given an integer, convert it to a roman numeral.

Example 1:
Input: num = 3749
Output: "MMMDCCXLIX"

Example 2:
Input: num = 58
Output: "LVIII"

Example 3:
Input: num = 1994
Output: "MCMXCIV"
"""


class Solution:
    def intToRoman(self, num: int) -> str:
        lroma = ['I', 'V', 'X', 'L', 'C', 'D', 'M']
        swich = {
            '0': [],
            '1': [0],
            '2': [0, 0],
            '3': [0, 0, 0],
            '4': [0, 1],
            '5': [1],
            '6': [1, 0],
            '7': [1, 0, 0],
            '8': [1, 0, 0, 0],
            '9': [0, 2]
        }

        def tiroma(n, m):
            re = ''

            for mi in swich[m]:
                re += lroma[n * 2 + mi]
            return re

        res = ''
        n = 0
        for i in str(num)[::-1]:
            res = tiroma(n, i) + res
            n += 1
        return res


if __name__ == "__main__":
    solution = Solution()
    print("Example 1:", solution.intToRoman(3749))  # Expected: "MMMDCCXLIX"
    print("Example 2:", solution.intToRoman(58))    # Expected: "LVIII"
    print("Example 3:", solution.intToRoman(1994))  # Expected: "MCMXCIV"
