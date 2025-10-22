from collections import defaultdict
import bisect
class Solution:
    # Only difference with 3346 is constraints, from 1e5 to 1e9 all
    def maxFrequency(self, nums: list[int], k: int, numOperations: int) -> int:
        nums.sort()
        best = 0
        cnt = defaultdict(int)
        potential_targets = set()

        for num in nums:
            cnt[num] += 1

        for num in nums:
            potential_targets.add(num)
            if num-k >= nums[0]:
                potential_targets.add(num-k)
            
        for x in sorted(potential_targets):
            left_bound = bisect.bisect_left(nums, x-k)
            right_bound = bisect.bisect_right(nums, x+k)-1
            if x in cnt:
                # A num being considered as the target value
                best = max(best, min(right_bound - left_bound + 1, cnt[x] + numOperations))
            else:
                # Not a num, but rather a left edge of a window
                best = max(best, min(right_bound - left_bound + 1, numOperations))
            
        return best


sol = Solution()
nums = [5,11,20,20]
k = 5
numOperations = 1
print(sol.maxFrequency(nums, k, numOperations))