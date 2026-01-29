from typing import List
from collections import defaultdict
from sortedcontainers import SortedList

from typing import List
from sortedcontainers import SortedList

class Solution:
    def minCost(self, grid: List[List[int]], k: int) -> int:
        m = len(grid)
        n = len(grid[0])

        sl = [(i, j) for i in range(m) for j in range(n)]
        sl.sort(key=lambda p: grid[p[0]][p[1]])

        dp = [[10**18 for _ in range(n)] for _ in range(m)]

        for k1 in range(k + 1):
            best = 10**18
            j = 0
            for i in range(len(sl)):
                x, y = sl[i]
                best = min(best, dp[x][y])
                if (i + 1 < len(sl) and grid[x][y] == grid[sl[i + 1][0]][sl[i + 1][1]]):
                    continue
                for r in range(j, i + 1):
                    xx, yy = sl[r]
                    dp[xx][yy] = best
                j = i + 1

            for i in range(m - 1, -1, -1):
                for j in range(n - 1, -1, -1):
                    if i == m - 1 and j == n - 1:
                        dp[i][j] = 0
                        continue
                    if i != m - 1:
                        dp[i][j] = min(dp[i][j], dp[i + 1][j] + grid[i + 1][j])
                    if j != n - 1:
                        dp[i][j] = min(dp[i][j], dp[i][j + 1] + grid[i][j + 1])

        return dp[0][0]




sol = Solution()
grid = [[1,3,3],[2,5,4],[4,3,5]]
k = 2
grid = [[3,5],[5,7]]
k = 0
grid = [[20,25,2],[15,22,15]]
k = 0
print(sol.minCost(grid, k))
