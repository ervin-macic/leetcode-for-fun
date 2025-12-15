from typing import List
class Solution:
    def getDescentPeriods(self, prices: List[int]) -> int:
        ans = 0
        n = len(prices)
        idx = 0
        while idx < n:
            descent = 1
            while idx < n-1 and prices[idx+1] - prices[idx] == -1:
                descent += 1
                idx += 1
            idx += 1
            ans += (descent*descent + descent) // 2
        return ans


sol = Solution()
prices = [3,2,1,4]
# There are 7 smooth descent periods:
# [3], [2], [1], [4], [3,2], [2,1], and [3,2,1]
prices = [8,6,7,7]
prices = [1]
print(sol.getDescentPeriods(prices))