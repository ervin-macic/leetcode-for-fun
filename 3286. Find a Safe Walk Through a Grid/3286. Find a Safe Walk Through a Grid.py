from collections import deque
from typing import List
class Solution:
    def findSafeWalk(self, grid: List[List[int]], health: int) -> bool:
        m, n = len(grid), len(grid[0])
        d = [[float("inf") for _ in range(n)] for _ in range(m)]
        d[0][0] = grid[0][0]
        q = deque()
        q.append((0, 0))
        while q:
            (i, j) = q.popleft()
            print((i, j))
            for ni, nj in [(i+1, j), (i, j+1), (i-1, j), (i, j-1)]:
                if 0 <= ni < m and 0 <= nj < n:
                    # frontier update
                    if d[i][j] + grid[ni][nj] < d[ni][nj]:
                        d[ni][nj] = d[i][j] + grid[ni][nj]
                        if grid[ni][nj] == 0:
                            q.appendleft((ni, nj))
                        else:
                            q.append((ni, nj))
        return health > d[m-1][n-1] 
sol = Solution()
grid = [[0,1,1,0,0,0],[1,0,1,0,0,0],[0,1,1,1,0,1],[0,0,1,0,1,0]]
health = 3
print(sol.findSafeWalk(grid, health))