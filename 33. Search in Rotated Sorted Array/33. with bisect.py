from typing import List 
from bisect import bisect_left
class Solution:
    def search(self, nums: List[int], target: int) -> int:
        idx = bisect_left(nums, (target <= nums[-1], target), key=lambda num: (num <= nums[-1], num))
        return idx if idx < len(nums) and nums[idx] == target else -1
sol = Solution()
nums = [4,5,6,7,0,1,2]
target = 0
print(sol.search(nums, target))