from typing import List
class Solution:
    def largestMagicSquare(self, grid: List[List[int]]) -> int:
        m = len(grid)
        n = len(grid[0])
        max_dim = min(m, n) + 1
        row_cum_sum = [[0] for _ in range(m)]
        col_cum_sum = [[0] for _ in range(n)]
        for i in range(m):
            for j in range(n):
                row_cum_sum[i].append(row_cum_sum[i][-1] + grid[i][j])
                col_cum_sum[j].append(col_cum_sum[j][-1] + grid[i][j])

        def ok(k: int) -> bool:
            nonlocal grid, m, n 
            for i in range(m - k + 1):
                for j in range(n - k + 1):
                    # Check whether the (k x k) square with top left corner at (i,j) is magic square
                    ij_good = True
                    common_sum = row_cum_sum[i][j+k] - row_cum_sum[i][j]
                    for K in range(k):
                        if (row_cum_sum[i+K][j+k] - row_cum_sum[i+K][j]) != common_sum:
                            ij_good = False
                            break
                        if (col_cum_sum[j+K][i+k] - col_cum_sum[j+K][i]) != common_sum:
                            ij_good = False
                            break
                    left_diag_sum = 0
                    right_diag_sum = 0
                    for d in range(k):
                        left_diag_sum += grid[i+d][j+d]
                        right_diag_sum += grid[i+d][j+k-1-d]
                    if left_diag_sum != common_sum or right_diag_sum != common_sum:
                        ij_good = False
                    if ij_good:
                        return True
            return False
        for dim in range(max_dim-1, -1, -1):
            if ok(dim):
                return dim

sol = Solution()
grid = [[7,1,4,5,6],[2,5,1,6,4],[1,5,4,3,2],[1,2,7,3,4]]
print(sol.largestMagicSquare(grid))