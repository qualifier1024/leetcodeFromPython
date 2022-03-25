"3"


class Solution(object):
    def isMatch(self, s, p):
        """
        :type s: str
        :type p: str
        :rtype: bool
        """
        los, t_end, tes = '*', [], 0
        for i in list(p):
            if i == '*':
                if los == '*':
                    return False
                else:
                    t_end += [tes, tes]
            elif los != '*':
                tes += 1
                t_end += [tes]
            los = i
        if p[-1] != '*':
            t_end += [tes + 1]

        def isTrue(o_s, o_p):
            if o_p == '.' or o_p == o_s:
                return True
            return False

        g_act = [[len(s) - 1, len(p) - 1]]
        for act in g_act:
            [si, pi] = act
            if si == -1 and (pi == -1 or t_end[pi] == 0):
                return True
            elif si > -1 and pi > -1:
                if p[pi] == '*' and pi:
                    cp = p[pi - 1]
                    csi = si
                    while csi != -1 and isTrue(s[csi], cp):
                        g_act.append([csi, pi - 2])
                        csi -= 1
                    g_act.append([csi, pi - 2])
                elif isTrue(s[si], p[pi]):
                    g_act.append([si - 1, pi - 1])
        return False