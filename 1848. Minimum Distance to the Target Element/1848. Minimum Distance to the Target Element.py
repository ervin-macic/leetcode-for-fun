from typing import List
class Solution:
    def getMinDistance(self, nums: List[int], target: int, start: int) -> int:
        # look left
        left = 10**10
        i = start 
        while i >= 0 and nums[i] != target:
            i -= 1
        if i >= 0 and nums[i] == target:
            left = i 
        
        # look right
        right = 10**10
        i = start 
        while i < len(nums) and nums[i] != target:
            i += 1
        if i < len(nums) and nums[i] == target:
            right = i 
        return min(abs(right-start), abs(left-start))

sol = Solution()
nums = [1,2,3,4,5]
target = 5
start = 3
print(sol.getMinDistance(nums, target, start))