from typing import List
from collections import defaultdict
class Solution:
    def solveQueries(self, nums: List[int], queries: List[int]) -> List[int]:
        val_to_indices = defaultdict(list)
        idx_to_idx = defaultdict(int)
        for i, num in enumerate(nums):
            idx_to_idx[i] = len(val_to_indices[num])
            val_to_indices[num].append(i)
        ans = []
        for q in queries:
            targets = val_to_indices[nums[q]]
            if len(targets) == 1:
                ans.append(-1)
            else:
                idx = idx_to_idx[q]
                left_dist, right_dist = 10**10, 10**10
                left_idx = targets[(idx - 1) % len(targets)] 
                right_idx = targets[(idx + 1) % len(targets)]
                left_dist = q - left_idx 
                right_dist = right_idx - q
                if idx == len(targets) - 1:
                    right_dist = right_idx + len(nums) - q
                elif idx == 0:
                    left_dist = q + len(nums) - left_idx
                ans.append(min(left_dist, right_dist))
        return ans
sol = Solution()
nums = [1,3,1,4,1,3,2]
queries = [0,3,5]
# left + 1 is 0 (since left = n-1), targets[left+1] = 1 actual q at 5 so should be (1+7) - 5 = 3 instead of |5-1| = 4 
# left_idx = idx + len(nums) - left_idx 
print(sol.solveQueries(nums, queries))

