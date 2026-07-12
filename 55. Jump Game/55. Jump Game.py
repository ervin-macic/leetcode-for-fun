from typing import List

class Solution:
    def canJump(self, nums: List[int]) -> bool:
        n = len(nums)
        curr = nums[0]
        for i in range(1, n):
            curr -= 1
            if curr < 0:
                return False
            curr = max(curr, nums[i])
        return True

sol = Solution()
nums = [2,3,1,1,4]
print(sol.canJump(nums))
            