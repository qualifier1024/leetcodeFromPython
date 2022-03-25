"2"


class Solution(object):
    def myAtoi(self, s):
        """
        :type s: str
        :rtype: int
        """
        int_li = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
        st = '0'
        ab = 1
        Flag =True
        for i in list(s):
            if i == '-' and Flag:
                ab =-1
                Flag =False
            elif i == '+' and Flag:
                Flag =False
            elif i in int_li:
                st = st + i
                Flag =False
            elif i == ' ' and Flag:
                pass
            else:
                break
        if int(st) >> 31 != 0:
            st = 2147483647 if ab ==1 else -2147483648
        else:
            st = int(st) *ab
        return st