import math
class Solution:
    def champagneTower(self, poured: int, query_row: int, query_glass: int) -> float:
        r, c = query_row, query_glass
        g = [[0 for _ in range(100)] for _ in range(100)]
        g[0][0] = float(poured)
        i = 0
        while i <= r:
            j = 0
            while j <= i:
                overflow = max(0, (g[i][j] - 1) / 2)
                g[i+1][j] += overflow
                g[i+1][j+1] += overflow
                j += 1
            i += 1
        return min(1, g[r][c])
sol = Solution()
poured = 2
query_row = 1
query_glass = 1
poured = 100000009
query_row = 33
query_glass = 17
print(sol.champagneTower(poured, query_row, query_glass))