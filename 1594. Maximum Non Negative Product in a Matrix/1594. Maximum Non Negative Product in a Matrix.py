class Solution:
    def maxProductPath(self, grid: list[list[int]]) -> int:
        MOD = 10**9 + 7
        m = len(grid)
        n = len(grid[0])
        dp = [[[None, None] for _ in range(n)] for _ in range(m)]

        if grid[0][0] >= 0:
            dp[0][0] = [grid[0][0], None]
        else:
            dp[0][0] = [None, grid[0][0]]
        
        for i in range(1, m):
            x = grid[i][0]
            prev = dp[i-1][0]
            curr = dp[i][0]
            if x >= 0:
                if prev[0] is not None:
                    curr[0] = prev[0] * x
                
                if prev[1] is not None:
                    curr[1] = prev[1] * x
            else:
                if prev[0] is not None:
                    curr[1] = prev[0] * x
                
                if prev[1] is not None:
                    curr[0] = prev[1] * x 
        
        for j in range(1, n):
            x = grid[0][j]
            prev = dp[0][j-1]
            curr = dp[0][j]
            if x >= 0:
                if prev[0] is not None:
                    curr[0] = prev[0] * x
                
                if prev[1] is not None:
                    curr[1] = prev[1] * x
            else:
                if prev[0] is not None:
                    curr[1] = prev[0] * x
                
                if prev[1] is not None:
                    curr[0] = prev[1] * x 
        
        for i in range(1, m):
            for j in range(1, n):
                x = grid[i][j]
                candidates = []
                for val in (dp[i-1][j][0], dp[i-1][j][1], dp[i][j-1][0], dp[i][j-1][1]):
                    if val is not None:
                        candidates.append(val * x)

                if candidates:
                    maxi = max(candidates)
                    mini = min(candidates)
                    dp[i][j][0] = maxi if maxi >= 0 else None
                    dp[i][j][1] = mini if mini <= 0 else None
        print(dp)
        if dp[m-1][n-1][0] is not None:
            return dp[m-1][n-1][0] % MOD
        else:
            return -1

sol = Solution()
grid = [[1,-2,1],[1,-2,1],[3,-4,1]]
grid = [[-1,-2,-3],[-2,-3,-3],[-3,-3,-2]]
grid = [[-1,3,0],[3,-2,3],[-1,1,-4]]
print(sol.maxProductPath(grid))