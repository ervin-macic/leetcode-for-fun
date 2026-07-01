from collections import deque 
from typing import List 
from bisect import bisect_left

class Solution:
    def maximumSafenessFactor(self, grid: List[List[int]]) -> int:
        n = len(grid)
        q = deque()
        dist = [[float("inf") for _ in range(n)] for _ in range(n)]
        for i in range(n):
            for j in range(n):
                if grid[i][j] == 1:
                    dist[i][j] = 0
                    q.append((i,j))

        while q:
            i, j = q.popleft()
            for ni, nj in [(i+1,j), (i-1,j), (i,j+1), (i,j-1)]:
                if 0 <= ni < n and 0 <= nj < n:
                    if dist[ni][nj] == float("inf"):
                        dist[ni][nj] = dist[i][j] + 1
                        q.append((ni, nj))
        
        # find best path using binary search on answer
        def existsPath(v) -> bool:
            visited = [[False for _ in range(n)] for _ in range(n)]
            def dfs(i, j, v) -> bool:
                if dist[i][j] < v:
                    return False
                if i == n-1 and j == n-1:
                    return True
                for ni, nj in [(i+1,j), (i-1,j), (i,j+1), (i,j-1)]:
                    if 0 <= ni < n and 0 <= nj < n and not visited[ni][nj] and dist[ni][nj] >= v:
                        visited[ni][nj] = True
                        if dfs(ni, nj, v):
                            return True 
                return False
            visited[0][0] = True
            return dfs(0, 0, v)
        idx = bisect_left(range(400, -1, -1), True, key=existsPath)
        return 400 - idx
                
sol = Solution()
grid = [[0,0,0,1],[0,0,0,0],[0,0,0,0],[1,0,0,0]]
print(sol.maximumSafenessFactor(grid))