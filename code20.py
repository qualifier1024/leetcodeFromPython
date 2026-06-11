"""
20. Valid Parentheses / 有效的括号 (Easy)

给定一个只包括 '('，')'，'{'，'}'，'['，']' 的字符串 s，判断字符串是否有效。
有效字符串需满足：
1. 左括号必须用相同类型的右括号闭合。
2. 左括号必须以正确的顺序闭合。
3. 每个右括号都有一个对应的相同类型的左括号。

Given a string s containing just the characters '(', ')', '{', '}', '[' and ']', determine if the input string is valid.

Example 1:
Input: s = "()"
Output: true

Example 2:
Input: s = "()[]{}"
Output: true

Example 3:
Input: s = "(]"
Output: false
"""


class Solution:
    def isValid(self, s: str) -> bool:
        lis = []
        lsd = {
            ')': '(',
            ']': '[',
            '}': '{'
        }
        for i in s[::1]:
            if i in ['(', '[', '{']:
                lis.append(i)
            else:
                if not lis:
                    return False
                if lis[-1] != lsd[i]:
                    return False
                lis.pop()
        if lis:
            return False
        return True


if __name__ == "__main__":
    solution = Solution()
    print("Example 1:", solution.isValid("()"))       # Expected: True
    print("Example 2:", solution.isValid("()[]{}"))   # Expected: True
    print("Example 3:", solution.isValid("(]"))       # Expected: False
