from typing import List
class Solution:
    def maxRotateFunction(self, nums: List[int]) -> int:
        ans = 0
        s = sum(nums)
        n = len(nums)
        curr = 0
        for i, num in enumerate(nums):
            curr += i * num
        ans = curr 
        for i in range(1, n):
            # fk = f(k-1) + s - n * nums[n-k]
            # have f0 ready in curr
            curr += s
            curr -= n * nums[n-i]
            ans = max(ans, curr)
        return ans
sol = Solution()
nums = [4,3,2,6]
print(sol.maxRotateFunction(nums))