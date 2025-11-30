from typing import List
from collections import defaultdict
from itertools import accumulate
class Solution:
    def minSubarray(self, nums: List[int], p: int) -> int:
        target = sum(nums) % p
        if target == 0:
            return 0
        cumsum = 0
        most_recent = {0: -1}
        best = len(nums)
        for i, x in enumerate(nums):
            cumsum = (cumsum + x) % p
            needed = (cumsum - target) % p
            if needed in most_recent:
                best = min(best, i - most_recent[needed])
            most_recent[cumsum] = i
        return best if best < len(nums) else -1

nums = [6,3,5,2]
p = 9
nums = [8,32,31,18,34,20,21,13,1,27,23,22,11,15,30,4,2]
p = 148 # should be 7
sol = Solution()
print(sol.minSubarray(nums, p))
            # r = cumsum % p - target_residue if target_residue <= cumsum % p else p + cumsum % p - target_residue


