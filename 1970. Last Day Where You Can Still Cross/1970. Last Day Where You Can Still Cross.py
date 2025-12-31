from typing import List 
from collections import defaultdict
class DSU:
    def __init__(self, n):
        self.root = [i for i in range(n)]
        self.size = [1 for _ in range(n)]

    def find(self, x):
        if self.root[x] != x:
            self.root[x] = self.find(self.root[x])
        return self.root[x]

    def union(self, x, y):
        root_x = self.find(x)
        root_y = self.find(y)
        if root_x == root_y:
            return
        if self.size[root_x] > self.size[root_y]:
            root_x, root_y = root_y, root_x
        self.root[root_x] = root_y
        self.size[root_y] += self.size[root_x]

class Solution:
    def latestDayToCross(self, row: int, col: int, cells: List[List[int]]) -> int:
        water = defaultdict(bool)
        dsu = DSU(row * col + 2)
        for (day, (r,c)) in enumerate(cells):
            r, c = r-1, c-1
            water[(r,c)] = True
            this_component = r * col + c + 1
            for dx in range(-1,2):
                for dy in range(-1,2):
                    if not (dx == dy == 0) and 0 <= r+dx < row and 0 <= c+dy < col and water[(r+dx, c+dy)]:
                        neighbor_component = (r + dx) * col + (c + dy) + 1
                        dsu.union(this_component, neighbor_component)
            if c == 0:
                dsu.union(0, this_component)
            if c == col - 1:
                dsu.union(row * col + 1, this_component)
            if dsu.find(0) == dsu.find(row * col + 1):
                return day
sol = Solution()
row = 2
col = 2
cells = [[1,1],[1,2],[2,1],[2,2]]
print(sol.latestDayToCross(row, col, cells))

