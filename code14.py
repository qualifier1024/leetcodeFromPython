from typing import List


def longestCommonPrefix(self, strs: List[str]) -> str:
    ans = ''
    for i in list(zip(*strs)):
        if len(set(i)) == 1:
            ans += i[0]
        else:
            break
    return ans


class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        ans = ''
        for i in list(zip(*strs)):
            if len(set(i)) == 1:
                ans += i[0]
            else:
                break
        return ans


if __name__ == "__main__":
    solution = Solution()
    print(solution.longestCommonPrefix(["flower","flow","flight"]))