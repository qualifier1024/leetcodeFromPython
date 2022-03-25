"2"


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