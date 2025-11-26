class Solution:
    def numberOfPaths(self, grid: list[list[int]], k: int) -> int:
        m = len(grid) # rows
        n = len(grid[0]) # columns
        dp = [[[0 for _ in range(k)] for _ in range(n)] for _ in range(m)]
        
        # Set first row and first column as base case
        cumsum = 0
        for i in range(m):
            cumsum += grid[i][0]
            dp[i][0][cumsum % k] = 1
        cumsum = 0
        for j in range(n):
            cumsum += grid[0][j]
            dp[0][j][cumsum % k] = 1
        
        MOD = 10**9 + 7
        # Update dp(i,j)'s residue paths based on left and up dp
        for i in range(1,m):
            for j in range(1,n):
                for r in range(k):
                    if dp[i][j-1][r] != 0:
                        dp[i][j][(r+grid[i][j]) % k] += dp[i][j-1][r]
                    if dp[i-1][j][r] != 0:
                        dp[i][j][(r+grid[i][j]) % k] += dp[i-1][j][r]

        return (dp[m-1][n-1][0] % MOD) 
sol = Solution()
grid = [[7,3,4,9],[2,3,6,2],[2,3,7,0]]
k = 1
grid = [[0,0]]
k = 5
grid = [[5,2,4],[3,0,5],[0,7,2]]
k = 3
print(sol.numberOfPaths(grid, k))