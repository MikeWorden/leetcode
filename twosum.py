import re
from typing import List

class Solution:
    #BruteForce -- O(n2) complexity
    def twoSum1(self, nums: List[int], target: int) -> List[int]:
        val = []
        for i in range(len(list)):
            for j in range(len(list)):
                if i == j:
                    pass
                else:
                    if nums[i] + nums[j] == target:
                        val.append(i)
                        val.append(j)
                        return val
        return val

    
    # Still Bruteforce, but exits when found
    def twoSum2(self, nums: List[int], target: int) -> List[int]:
        val=[]
        for i in range(target):
            num1 = target - i
            num2 = i
            try:
                index1 = nums.index(num1)
                index2 = nums.index(num2)
                if (index1 != index2):
                    val.append(index1)
                    val.append(index2)
                    val.sort()
                    return val
            except:
                next
        return val

    # Faster with dict lookups    
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        
        numsHash = dict()

        for i in range(len(nums)):
            numsHash[nums[i]] = i
        #print(numsHash)
        val=[]
        found = False
        i = 0
        numsLength = len(nums)
        while (not found) and (i < numsLength):
            num1 = nums[i]
            num2 = target - num1
            
            if (num2 in numsHash) and (i != numsHash[num2]):
                    val.append(i)
                    val.append(numsHash[num2])
                    found = True
            i += 1
        return val


list = [3, 2, 4]
target = 6

sol = Solution()


print(sol.twoSum(list, target))
