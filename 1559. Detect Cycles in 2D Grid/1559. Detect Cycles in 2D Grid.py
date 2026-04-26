from typing import List
from collections import defaultdict 
class Solution:
    def containsCycle(self, grid: List[List[str]]) -> bool:
        m, n = len(grid), len(grid[0]) 
        visited = defaultdict(bool)
        def dfs(node: (int, int), parent: (int, int)):
            (i, j) = node
            visited[node] = True
            candidates = []
            for (dx, dy) in [(-1, 0), (0, -1), (1, 0), (0, 1)]:
                if 0 <= i + dx < m and 0 <= j + dy < n and grid[i + dx][j + dy] == grid[i][j]:
                    if not visited[(i + dx, j + dy)]:
                        if dfs((i + dx, j + dy), node):
                            return True
                    elif (i + dx, j + dy) != parent:
                        return True
            return False
        for r in range(m):
            for c in range(n):
                if not visited[(r, c)]:
                    if dfs((r, c), (None, None)):
                        return True
        return False

sol = Solution()
grid = [["a","a","a","a"],["a","b","b","a"],["a","b","b","a"],["a","a","a","a"]]
print(sol.containsCycle(grid))
                