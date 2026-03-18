class Solution:
    def countSubmatrices(self, grid: list[list[int]], k: int) -> int:
        total = 0
        m = len(grid)
        n = len(grid[0])
        square_sum = [[0 for _ in range(n+1)] for _ in range(m+1)]
        for i in range(1, m+1):
            for j in range(1, n+1):
                square_sum[i][j] = grid[i-1][j-1] + square_sum[i-1][j] + square_sum[i][j-1] - square_sum[i-1][j-1]
                if square_sum[i][j] <= k:
                    total += 1
        return total

        
sol = Solution()
grid = [[7,2,9],
        [1,5,0],
        [2,6,6]]
k = 20
grid = [[7,6,3],[6,6,1]]
k = 18
print(sol.countSubmatrices(grid, k))