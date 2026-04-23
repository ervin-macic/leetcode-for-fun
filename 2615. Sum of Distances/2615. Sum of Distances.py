from typing import List
from collections import defaultdict
class Solution:
    def distance(self, nums: List[int]) -> List[int]:
        left = [0 for _ in range(len(nums))]
        indices = defaultdict(list)
        for i, num in enumerate(nums):
            prev_i = i
            if len(indices[num]) > 0:
                prev_i = indices[num][-1] # previous index with value num
            left[i] += len(indices[num]) * (i - prev_i) + left[prev_i]
            indices[num].append(i)
        
        right = [0 for _ in range(len(nums))]
        indices = defaultdict(list)
        for i, num in reversed(list(enumerate(nums))):
            prev_i = i
            if len(indices[num]) > 0:
                prev_i = indices[num][-1] # previous index with value num
            right[i] += len(indices[num]) * (prev_i - i) + right[prev_i]
            indices[num].append(i)
        return [l+r for l,r in zip(left, right)]

sol = Solution()
nums = [1,3,1,1,2]
print(sol.distance(nums))
