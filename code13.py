"1"


class Solution:
    def romanToInt(self, s: str) -> int:
        sni =0
        snm=0
        roma={
            'I':1,
            'V':5,
            'X':10,
            'L':50,
            'C':100,
            'D':500,
            'M':1000
        }
        for i in s[::-1]:
            ni=roma[i]
            if ni>=sni:
                snm+=ni
                sni=ni
            else:
                snm-=ni
        return snm