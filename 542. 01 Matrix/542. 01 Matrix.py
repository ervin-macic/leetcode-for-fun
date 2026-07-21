from typing import List
from collections import deque, defaultdict
class Solution:
    def updateMatrix(self, mat: List[List[int]]) -> List[List[int]]:
        m, n = len(mat), len(mat[0])
        ans = [[float("inf") for _ in range(n)] for _ in range(m)]
        q = deque()
        visited = [[False for _ in range(n)] for _ in range(m)]
        for i in range(m):
            for j in range(n):
                if mat[i][j] == 0:
                    q.append((i,j))
                    visited[i][j] = True
                    ans[i][j] = 0
        dirs = [(0,1), (0,-1), (1,0), (-1,0)]
        while q:
            i, j = q.popleft()
            for dx, dy in dirs:
                x, y = i + dx, j + dy 
                if 0 <= x < m and 0 <= y < n and not visited[x][y]:
                    q.append((x,y))
                    ans[x][y] = min(ans[x][y], ans[i][j] + 1)
                    visited[x][y] = True
        return ans

sol = Solution()
mat = [[0,0,0],[0,1,0],[1,1,1]]
mat = [[1,0,1,1,0,0,1,0,0,1],[0,1,1,0,1,0,1,0,1,1],[0,0,1,0,1,0,0,1,0,0],[1,0,1,0,1,1,1,1,1,1],[0,1,0,1,1,0,0,0,0,1],[0,0,1,0,1,1,1,0,1,0],[0,1,0,1,0,1,0,0,1,1],[1,0,0,0,1,1,1,1,0,1],[1,1,1,1,1,1,1,0,1,0],[1,1,1,1,0,1,0,0,1,1]]
print(sol.updateMatrix(mat))

                
