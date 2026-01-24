from typing import List
class Solution:
    def minPairSum(self, nums: List[int]) -> int:
        nums.sort()
        max_pair_sum = -10**9+7
        n = len(nums)
        i = 0
        j = n - 1
        while i < j:
            max_pair_sum = max(max_pair_sum, nums[i] + nums[n-i-1])
            i += 1
            j -= 1
        return max_pair_sum

sol = Solution()
nums = [3,5,4,2,4,6]
print(sol.minPairSum(nums))