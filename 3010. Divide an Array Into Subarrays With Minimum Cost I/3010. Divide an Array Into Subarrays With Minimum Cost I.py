from typing import List
class Solution:
    def minimumCost(self, nums: List[int]) -> int:
        ans = nums[0]
        n = len(nums)
        min = float("inf")
        min_idx = None
        for i in range(1, n):
            if nums[i] < min:
                min = nums[i]
                min_idx = i
        min2 = float("inf")
        min_idx2 = None 
        for j in range(1, n):
            if nums[j] < min2 and j != min_idx:
                min2 = nums[j]
                min_idx2 = j
        return ans + min + min2
sol = Solution()
nums = [10,3,1,1]
print(sol.minimumCost(nums))