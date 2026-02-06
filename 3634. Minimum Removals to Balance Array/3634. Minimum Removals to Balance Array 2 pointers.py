from typing import List
from bisect import bisect_right
class Solution:
    def minRemoval(self, nums: List[int], k: int) -> int:
        nums.sort()
        n = len(nums)
        ans = n
        l = 0
        r = 0
        while l < n:
            while r < n and nums[r] <= k*nums[l]:
                r += 1
            ans = min(ans, n - (r - l))
            l += 1
        return ans

sol = Solution()
nums = [1,6,2,9]
k = 3
nums = [4,6]
k = 2
nums = [1,34,23]
k = 2
print(sol.minRemoval(nums, k))