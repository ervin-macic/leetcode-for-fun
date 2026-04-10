from typing import List
from collections import defaultdict
class Solution:
    def minimumDistance(self, nums: List[int]) -> int:
        hash = defaultdict(list)
        min_dist = 10**9+7
        for i, num in enumerate(nums):
            if len(hash[num]) > 1:
                min_dist = min(min_dist, i - hash[num][-2])
            hash[num].append(i)
        
        if min_dist == 10**9+7:
            return -1
        return 2 * min_dist 

sol = Solution()
nums = [3,3,3]
print(sol.minimumDistance(nums))
