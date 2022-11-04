from typing import List


class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        
        #merge the arrays
        l = 0   #index of left array(nums1)
        r = 0   #index of right array (nums2)
        c = 0   #index of merged array (nums3)

        lLength = len(nums1)
        rLength = len(nums2)
        nums3 = [None] * (lLength + rLength)



        while l < lLength and r < rLength:
            if nums1[l] < nums2[r]:
                nums3[c] = nums1[l]
                l += 1
                c += 1
            else:
                nums3[c] = nums2[r]
                r += 1
                c += 1

        # at this point, either the left (nums1) or right (nums2)
        # array is empty.  Now we append from whatever array still has elements

        while l < lLength:
            nums3[c] = nums1[l]
            l += 1
            c += 1

        while r < rLength:
            nums3[c]  = nums2[r]
            r += 1
            c += 1

        print(nums3)
        n = len(nums3)
        ans = (nums3[n//2 -1]/2.0 + nums3[n//2]/2.0, nums3[n//2])[n % 2] if n else None
        #ans = 42.0

        return float(ans)



nums1 = [1,3] 
nums2 = [2]

nums1 = [1,2]
nums2 = [3,4]

sol = Solution()

print(sol.findMedianSortedArrays(nums1, nums2))