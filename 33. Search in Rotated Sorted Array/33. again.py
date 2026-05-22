from typing import List 
from bisect import bisect_left
class Solution:
    def search(self, nums: List[int], target: int) -> int:
        def bisectLeft(nums, target, key):
            l = 0
            r = len(nums)
            # Invariant: nums[0..i) < target <= nums[j..n)
            while l < r:
                m = (r - l) // 2 + l
                if key(nums[m]) < target:
                    i = m + 1
                else:
                    j = m
            return l
        i = bisectLeft(nums, (target <= nums[-1], target), key=lambda x: (x <= nums[-1], x))
        return i if i < len(nums) and nums[i] == target else -1