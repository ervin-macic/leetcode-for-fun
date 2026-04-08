from typing import List
class Solution:
    def xorAfterQueries(self, nums: List[int], queries: List[List[int]]) -> int:
        MOD = 10**9 + 7
        for l, r, k, v in queries:
            for idx in range(l, r+1, k):
                nums[idx] = (nums[idx] * v) % MOD
        ans = 0
        for x in nums:
            ans ^= x
        return ans
sol = Solution()
nums = [2,3,1,5,4]
queries = [[1,4,2,3],[0,2,1,2]]
print(sol.xorAfterQueries(nums, queries))