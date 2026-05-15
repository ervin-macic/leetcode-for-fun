from typing import List 
class Solution:
    def findMin(self, nums: List[int]) -> int:
        if len(nums) == 1 or nums[0] < nums[-1]:
            return nums[0]
        n = len(nums)
        l = 0
        r = n
        while r-l > 2:
            m = (r-l) // 2 + l 
            if nums[m] > nums[r-1]:
                l = m + 1
            elif nums[m] < nums[r-1]:
                r = m + 1
        return nums[l]
sol = Solution()
nums = [13,14,17,1,2,3,5,8,10]
nums = [10]
nums = [2,3,1]
print(sol.findMin(nums))
                
        
    