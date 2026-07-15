import time
class Solution:
    def firstMissingPositive(self, nums: List[int]) -> int:
        i = 0
        n = len(nums)
        while i < n:
            if 1 <= nums[i] <= n and nums[i] != i+1 and nums[nums[i] - 1] != nums[i]:
                # swap nums[i] and nums[nums[i]-1]
                target = nums[i] - 1
                nums[i], nums[target] = nums[target], nums[i]
            else:
                i += 1
        
        for i in range(n):
            if nums[i] != i+1:
                return i+1
        return n+1
sol = Solution()
nums = [3,4,-1,-2,1,5,16,0,2,0]
print(sol.firstMissingPositive(nums))