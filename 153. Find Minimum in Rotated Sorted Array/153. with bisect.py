from typing import List 
from bisect import bisect_left
class Solution:
    def findMin(self, nums: List[int]) -> int:
        if len(nums) == 1 or nums[0] < nums[-1]:
            return nums[0]
        return nums[bisect_left(nums, True, key=lambda x: x <= nums[-1])]
sol = Solution()
nums = [13,14,17,1,2,3,5,8,10]
nums = [10]
nums = [2,3,1]
print(sol.findMin(nums))
                
        
    