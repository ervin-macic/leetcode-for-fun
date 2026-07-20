from typing import List
class Solution:
    def shiftGrid(self, grid: List[List[int]], k: int) -> List[List[int]]:
        m = len(grid)
        n = len(grid[0])
        ans = [[0 for _ in range(n)] for _ in range(m)] 
        for i in range(m):
            for j in range(n):
                row = ((n * i + j + k) % (m*n)) // n 
                col = (n * i + j + k) % n
                ans[row][col] = grid[i][j]
        return ans
sol = Solution()
grid = [[1,2,3],[4,5,6],[7,8,9]]
k = 2
ans = sol.shiftGrid(grid, k)
print(ans)