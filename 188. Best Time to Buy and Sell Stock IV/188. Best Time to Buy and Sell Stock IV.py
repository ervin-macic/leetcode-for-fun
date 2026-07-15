class Solution:
    def maxProfit(self, k: int, prices: List[int]) -> int:
        # dp[i][t][0/1] = max profit achievable at the end of day i
        # with exactly t completed transactions
        # 0 = not holding, 1 = long/holding
        n = len(prices)
        dp = [[[float("-inf") for _ in range(2)] for _ in range(k+1)] for _ in range(n)]

        # base cases
        dp[0][0][0] = 0
        dp[0][0][1] = -prices[0]

        for i in range(1, n):
            # 0 completed transactions
            dp[i][0][0] = dp[i-1][0][0]
            dp[i][0][1] = max(dp[i-1][0][0] - prices[i], dp[i-1][0][1])
            # t >= 1 completed transactions
            for t in range(1, k+1):
                # do nothing or sell today
                dp[i][t][0] = max(dp[i-1][t][0], dp[i-1][t-1][1] + prices[i])
                # do nothing or buy today
                dp[i][t][1] = max(dp[i-1][t][0] - prices[i], dp[i-1][t][1])
        return max(dp[n-1][t][0] for t in range(k+1))

sol = Solution()
k = 2
prices = [3,2,6,5,0,3]
print(sol.maxProfit(k, prices))