"""
22. Generate Parentheses / 括号生成 (Medium)

数字 n 代表生成括号的对数，请你设计一个函数，用于能够生成所有可能的并且有效的括号组合。

Given n pairs of parentheses, write a function to generate all combinations of well-formed parentheses.

Example 1:
Input: n = 3
Output: ["((()))","(()())","(())()","()(())","()()()"]

Example 2:
Input: n = 1
Output: ["()"]

Example 3:
Input: n = 2
Output: ["(())","()()"]
"""


from typing import List


class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        res = []

        def gp(los, a, b):
            if a == 0:
                res.append(los + ')' * b)
                return
            gp(los + '(', a - 1, b)
            if a < b:
                gp(los + ')', a, b - 1)

        gp('', n, n)
        return res


if __name__ == "__main__":
    solution = Solution()
    print("Example 1:", solution.generateParenthesis(3))  # Expected: ["((()))","(()())","(())()","()(())","()()()"]
    print("Example 2:", solution.generateParenthesis(1))  # Expected: ["()"]
    print("Example 3:", solution.generateParenthesis(2))  # Expected: ["(())","()()"]
