from typing import List

class Solution:
    def hasValidPath(self, grid: List[List[int]]) -> bool:
        m, n = len(grid), len(grid[0])
        dirs = {
            1: [(0,1), (0,-1)],
            2: [(1,0), (-1,0)],
            3: [(0,-1), (1,0)],
            4: [(0,1), (1,0)],
            5: [(0,-1), (-1,0)],
            6: [(0,1), (-1,0)],
        }
        seen = set()
        def dfs(i, j):
            if (i, j) == (m-1, n-1):
                return True
            seen.add((i, j))
            for di, dj in dirs[grid[i][j]]:
                ni, nj = i + di, j + dj
                if (
                    0 <= ni < m and 0 <= nj < n
                    and (ni, nj) not in seen
                    and (-di, -dj) in dirs[grid[ni][nj]]
                    and dfs(ni, nj)
                ):
                    return True
            return False
        return dfs(0, 0)
sol = Solution()
grid = [[2,4,3],[6,5,2]]
grid = [[2,6,3],[6,5,2]]
print(sol.hasValidPath(grid))