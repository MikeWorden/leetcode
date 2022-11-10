from bdb import Breakpoint
from typing import List, OrderedDict                                                         
from collections import Counter
from string import ascii_letters


class Solution:


    # Still slow, but passes...
    def longestPalindrome(self, s: str) -> str:
        ans = ""
        if len(s) <= 1:
            return s
        found = False
        l = len(s)
        for window in range(l, 0, -1):
            #create a 'window' substring from the string
            #then slide that window from the start to the end of the string
            steps = l - i        
            for step in range(steps+1):
                
                found = self.isPalindrome(s[step:window+step])
                #print(s[j:i+j], found )
                if found:
                    ans = s[step:step+window]
                    break                       #stop wihen found
            if found:
                break                           #stop when found

        
        return ans
    
    # Bruteforce -- slow
    def longestPalindrome2(self, s: str) -> str:
        ans = ""
        if len(s) <= 1:
            return s
        f = 0   # front
        b = 0   # back
        found = False
        l = len(s)
        while f < l:
            while (b < l) and (l-b >f) and (not found):
                
                if self.isPalindrome(s[f:l-b]):
                    if len(ans) < len(s[f:l-b]):
                        #print(s[f:l-b], self.isPalindrome(s[f:l-b]))
                        ans = s[f:l-b]
                    #found = True
                b += 1
            #if found:
                #break
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
sList = [ "cbbd", "babad", "abb"]
#sList = ["abb"]
#sList = ["babad", "abababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababa"]
sol = Solution()
for s in sList:
    print(sol.longestPalindrome(s))                                          

