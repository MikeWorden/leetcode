from typing import List                                                         
from collections import Counter
from string import ascii_letters


class Solution:
    def longestPalindrome(self, s: str) -> str:
        ans = ""
        if len(s) <= 1:
            return s
        f = 0   # front
        b = 0   # back
        p = 0
        l = len(s)
        while f < l:
            while (b < l) and (l-b >f):
                #print(s[f:l-b], self.isPalindrome(s[f:l-b]))
                if self.isPalindrome(s[f:l-b]):
                    if len(s[f:l-b]) > len(ans):
                        ans = s[f:l-b]
                b += 1
            f += 1
            b = 0
        return ans

    def isPalindrome(self, s: str) -> bool:
        b = -1
        flag = True
        for i in s:
            if i != s[b]:
                flag = False
                break
            b = b - 1
        return flag

sList = ["abccccdd", "bb", "AB", "aba", "aBBc"]
sList = ["babad"]
sol = Solution()
for s in sList:
    print(sol.longestPalindrome(s))                                          

