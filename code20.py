"1"


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
