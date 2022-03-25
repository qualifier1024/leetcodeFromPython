"2"


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
