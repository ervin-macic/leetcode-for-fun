from typing import List 
from collections import deque 

class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        m, n = len(grid), len(grid[0])
        visited = grid
        q = deque()
        fresh_cnt = 0
        for i in range(m):
            for j in range(n):
                if visited[i][j] == 2:
                    q.append((i, j))
                if visited[i][j] == 1:
                    fresh_cnt += 1
        if fresh_cnt == 0: # no fresh oranges at all
            return 0
        if not q: # no rotten oranges at all
            return -1
        
        minutes = -1
        dirs = [(1, 0), (-1, 0), (0, -1), (0, 1)]
        while q:
            size = len(q)
            while size > 0:
                x, y = q.popleft()
                size -= 1
                for dx, dy in dirs:
                    i, j = x + dx, y + dy
                    if 0 <= i < m and 0 <= j < n and visited[i][j] == 1:
                        visited[i][j] = 2
                        fresh_cnt -= 1
                        q.append((i, j))
            minutes += 1
        
        if fresh_cnt == 0:
            return minutes
        return -1

sol = Solution()
grid = [[2,1,1],[1,1,0],[0,1,1]]
print(sol.orangesRotting(grid))