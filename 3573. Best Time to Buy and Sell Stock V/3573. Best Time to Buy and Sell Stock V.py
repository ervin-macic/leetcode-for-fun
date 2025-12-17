from typing import List
class Solution:
    def maximumProfit(self, prices: List[int], k: int) -> int:
        # max profit earnable after day pos, with exactly k transactions completed, being (0/1/2  OR nothing/long/short)
        
        n = len(prices)
        dp = [[[0 for _ in range(3)] for _ in range(k+1)] for _ in range(n)]
        
        for k1 in range(1, k+1):
            dp[0][k1][1] = -prices[0]
            dp[0][k1][2] = prices[0]
        for pos in range(1, n):
            for k1 in range(1, k+1):
                dp[pos][k1][0] = max(dp[pos-1][k1][1] + prices[pos],
                                     dp[pos-1][k1][2] - prices[pos], dp[pos-1][k1][0])
                dp[pos][k1][1] = max(dp[pos-1][k1-1][0] - prices[pos], dp[pos-1][k1][1])
                dp[pos][k1][2] = max(dp[pos-1][k1-1][0] + prices[pos], dp[pos-1][k1][2])

        return dp[n-1][k][0]

sol = Solution()
prices = [12,16,19,19,8,1,19,13,9]
k = 3
print(sol.maximumProfit(prices, k))