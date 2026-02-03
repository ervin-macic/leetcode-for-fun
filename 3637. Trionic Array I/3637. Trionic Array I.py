from typing import List
class Solution:
    def isTrionic(self, nums: List[int]) -> bool:
        p = 0
        n = len(nums)
        while p < n-1 and nums[p+1] > nums[p]:
            p += 1
        if p == 0 or p == n-1:
            return False
        q = n-1
        while q > 0 and nums[q] > nums[q-1]:
            q -= 1
        if q == n-1 or q == 0:
            return False 
        
        if p >= q:
            return False
        for i in range(p+1, q+1):
            if nums[i] >= nums[i-1]:
                return False 
        return True 
sol = Solution()
nums = [1,3,5,4,2,6]
nums = [2,1,3]
print(sol.isTrionic(nums))

        
        
