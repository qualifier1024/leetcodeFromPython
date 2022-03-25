"2"

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