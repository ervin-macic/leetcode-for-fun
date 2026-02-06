from typing import List
from bisect import bisect_right
class Solution:
    def minRemoval(self, nums: List[int], k: int) -> int:
        nums.sort()
        max_seg = 0
        n = len(nums)
        for i in range(n):
            j = bisect_right(nums, k*nums[i])
            # print(f"i: {i}, j: {j}, nums[i]: {nums[i]}, nums[j]: {nums[j]}")
            max_seg = max(max_seg, j-i)
        return (n-max_seg) if max_seg !=0 else 0

sol = Solution()
nums = [1,6,2,9]
k = 3
nums = [4,6]
k = 2
nums = [1,34,23]
k = 2
print(sol.minRemoval(nums, k))