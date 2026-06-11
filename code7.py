"""
7. Reverse Integer / 整数反转 (Medium)

给你一个 32 位的有符号整数 x，返回将 x 中的数字部分反转后的结果。
如果反转后整数超过 32 位有符号整数的范围 [−2^31, 2^31 − 1]，就返回 0。

Given a signed 32-bit integer x, return x with its digits reversed.
If reversing x causes the value to go outside the 32-bit signed integer range, return 0.

Example 1:
Input: x = 123
Output: 321

Example 2:
Input: x = -123
Output: -321

Example 3:
Input: x = 120
Output: 21
"""


class Solution(object):
    def reverse(self, x):
        """
        :type x: int
        :rtype: int
        """
        ab = -1 if x < 0 else 1
        s = int(str(abs(x))[::-1])
        if s >> 31 != 0:
            return 0
        return s * ab


if __name__ == "__main__":
    solution = Solution()
    print("Example 1:", solution.reverse(123))    # Expected: 321
    print("Example 2:", solution.reverse(-123))   # Expected: -321
    print("Example 3:", solution.reverse(120))    # Expected: 21
