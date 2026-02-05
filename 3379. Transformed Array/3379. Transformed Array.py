from typing import List
class Solution:
    def constructTransformedArray(self, nums: List[int]) -> List[int]:
        n = len(nums)
        result = [0] * n
        for i in range(n):
            result[i] = nums[(i + nums[i])%n]
        return result 

sol = Solution()
nums = [3,-2,1,1]
print(sol.constructTransformedArray(nums))