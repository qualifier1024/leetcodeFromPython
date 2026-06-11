"""
6. Zigzag Conversion / Z 字形变换 (Medium)

将一个给定字符串 s 根据给定的行数 numRows，以从上往下、从左到右进行 Z 字形排列。

The string "PAYPALISHIRING" is written in a zigzag pattern on a given number of rows.

Example 1:
Input: s = "PAYPALISHIRING", numRows = 3
Output: "PAHNAPLSIIGYIR"

Example 2:
Input: s = "PAYPALISHIRING", numRows = 4
Output: "PINALSIGYAHRPI"

Example 3:
Input: s = "A", numRows = 1
Output: "A"
"""


class Solution(object):
    def convert(self, s, numRows):
        """
        :type s: str
        :type numRows: int
        :rtype: str
        """
        if numRows == 1:
            return s
        res = ""
        nu = ['']*numRows
        al = 0
        n = 1
        for i in list(s):
            nu[al] = nu[al]+i
            if not 0 <= al+n < numRows:
                n = -n
            al = al + n
        for j in nu:
            res = res + j
        return res


if __name__ == "__main__":
    solution = Solution()
    print("Example 1:", solution.convert("PAYPALISHIRING", 3))  # Expected: "PAHNAPLSIIGYIR"
    print("Example 2:", solution.convert("PAYPALISHIRING", 4))  # Expected: "PINALSIGYAHRPI"
    print("Example 3:", solution.convert("A", 1))               # Expected: "A"
