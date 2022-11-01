from re import S
from typing import List, OrderedDict

class Solution:
    # Bruteforce approach -- O(n^2)
    def lengthOfLongestSubstring2(self, s: str) -> int:
        winlength = len(s)
        start = 0
        found = False
        ans = 0
        while (winlength >= 1) and (not found):
            while start+winlength <= len(s) and (not found):
                window = s[start:start+winlength]
                #print(window)
                noDups = "".join(OrderedDict.fromkeys(window))
                print(window, noDups)
                if window == noDups:
                    found = True
                    ans = len(window)
                start +=1
            winlength -=1
            start = 0
        return ans # 42 is the answer

    def lengthOfLongestSubstring(self, s: str) -> int:
        ans = 0
        
        sLength = len(s)
        #Short strings have an obvious solution
        if sLength <= 1:
            return sLength
        
        nonDupString = ""
        
        for c in s:
            # if c is already in the string, then move past the 1st occurence
            if c in nonDupString:       
                nonDupString = nonDupString[nonDupString.index(c)+1:]
            #and append
            nonDupString = nonDupString + c
            #figure out what's longest
            ans = max(ans, len(nonDupString))

        return ans 

s = ""
s = "abcabcbb"
s = "bbbbb"
s ="hijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789hijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789hijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789hijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789hijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789hijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789"

sol = Solution()

print(sol.lengthOfLongestSubstring(s))
