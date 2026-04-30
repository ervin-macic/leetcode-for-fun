from typing import List

class Solution:
    def maxPathScore(self, grid: List[List[int]], k: int) -> int:
        m, n = len(grid), len(grid[0])

        cost = {
            0: 0, 
            1: 1, 
            2: 1
            }

        dp = [[[-1] * (k + 1) for _ in range(n)] for _ in range(m)]
        dp[0][0][0] = 0

        for i in range(m):
            for j in range(n):
                if i == 0 and j == 0:
                    continue

                v = grid[i][j]
                w = cost[v]

                for c in range(w, k + 1):
                    best = -1
                    if i > 0 and dp[i - 1][j][c - w] != -1:
                        best = max(best, dp[i - 1][j][c - w] + v)

                    if j > 0 and dp[i][j - 1][c - w] != -1:
                        best = max(best, dp[i][j - 1][c - w] + v)
                    dp[i][j][c] = best

        return max(dp[m - 1][n - 1])