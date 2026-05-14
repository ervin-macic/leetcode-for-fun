from typing import List
class Solution:
    def isGood(self, nums: List[int]) -> bool:
        nums.sort()
        m = len(nums)
        n = m-1
        curr = n
        if nums[-1] != curr:
            return False
        for num in reversed(nums[:-1]):
            if num != curr:
                return False
            curr -= 1
        return True
