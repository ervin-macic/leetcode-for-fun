from typing import List
class Solution:
    def maximumAmount(self, coins: List[List[int]]) -> int:
        m, n = len(coins), len(coins[0])
        # dp[i][j][k] = max amount of money earnable starting at (0,0) ending at (i,j) using at most k powerups
        dp = [[[-float("inf") for _ in range(3)] for _ in range(n)] for _ in range(m)]

        dp[0][0][0] = coins[0][0]
        dp[0][0][1] = dp[0][0][2] = max(0, coins[0][0])

        for j in range(1, n):
            c = max(0, coins[0][j])
            dp[0][j][0] = coins[0][j] + dp[0][j-1][0]
            dp[0][j][1] = max(coins[0][j] + dp[0][j-1][1], c + dp[0][j-1][0])
            dp[0][j][2] = max(coins[0][j] + dp[0][j-1][2], c + dp[0][j-1][1])

        for i in range(1, m):
            c = max(0, coins[i][0])
            dp[i][0][0] = coins[i][0] + dp[i - 1][0][0]
            dp[i][0][1] = max(coins[i][0] + dp[i-1][0][1], c + dp[i-1][0][0])
            dp[i][0][2] = max(coins[i][0] + dp[i-1][0][2], c + dp[i-1][0][1])

        for i in range(1, m):
            for j in range(1, n):
                c = coins[i][j]
                dp[i][j][0] = c + max(dp[i-1][j][0], dp[i][j-1][0])
                dp[i][j][2] = max(c + dp[i-1][j][2], c + dp[i][j-1][2], dp[i-1][j][1], dp[i][j-1][1])
                dp[i][j][1] = max(c + dp[i-1][j][1], c + dp[i][j-1][1], dp[i-1][j][0], dp[i][j-1][0])

        return dp[m-1][n-1][2]
sol = Solution()
coins = [[0,1,-1],[1,-2,3],[2,-3,4]]
print(sol.maximumAmount(coins))