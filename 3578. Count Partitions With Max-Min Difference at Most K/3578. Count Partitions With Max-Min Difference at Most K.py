from typing import List
class Solution:
    def countPartitions(self, arr: List[int], limit: int) -> int:
        n = len(arr)
        MOD = 10**9 + 7

        dp = [0] * (n + 1)
        cumulative = [0] * (n + 1)
        window = SortedList()

        dp[0] = 1
        cumulative[0] = 1

        left = 0
        for right in range(n):
            window.add(arr[right])

            # shrink sliding window if condition is violated
            while left <= right and window[-1] - window[0] > limit:
                window.remove(arr[left])
                left += 1

            valid_sum = cumulative[right]
            if left > 0:
                valid_sum = (valid_sum - cumulative[left - 1]) % MOD

            dp[right + 1] = valid_sum
            cumulative[right + 1] = (cumulative[right] + dp[right + 1]) % MOD

        return dp[n]


sol = Solution()

nums = [3,3,4]
k = 0
nums = [9,4,1,3,7] # [9] [4,1,3] [7]
k = 4
print(sol.countPartitions(nums, k))