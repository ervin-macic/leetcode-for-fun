from typing import List
class Solution:
    def maxDistance(self, nums1: List[int], nums2: List[int]) -> int:
        # nums1 = [55,30,5,4,2], nums2 = [100,20,10,10,5]
        l = 0
        r = 0
        ans = 0
        for r in range(len(nums2)):
            while l < len(nums1) and nums1[l] > nums2[r]:
                l += 1
            # know nums1[l] <= nums2[r]
            if l < len(nums1) and l <= r:
                ans = max(ans, r-l)
        return ans
sol = Solution()
nums1 = [55,30,5,4,2]
nums2 = [100,20,10,10,5]
print(sol.maxDistance(nums1, nums2))
            