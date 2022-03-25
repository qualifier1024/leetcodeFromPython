"2"
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
