from collections import defaultdict 
import bisect
class Solution:
    def maxFrequency(self, nums: list[int], k: int, numOperations: int) -> int:
        nums.sort()
        best = 0
        cnt = defaultdict(int)
        for num in nums:
            cnt[num] += 1
        for x in range(nums[0], nums[-1]+1):
            left_bound = bisect.bisect_left(nums, x-k)
            right_bound = bisect.bisect_right(nums, x+k)-1
            best = max(best, min(right_bound - left_bound + 1, cnt[x] + numOperations))
        return best

sol = Solution()
nums = [5,11,20,20]
k = 5
numOperations = 1
print(sol.maxFrequency(nums, k, numOperations))

