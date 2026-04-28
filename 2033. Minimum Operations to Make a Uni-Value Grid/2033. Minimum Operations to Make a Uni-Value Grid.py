from typing import List
import numpy as np
class Solution:
    def minOperations(self, grid: List[List[int]], x: int) -> int:
        r = grid[0][0] % x
        arr = []
        for row in grid:
            for elem in row:
                arr.append(elem)
                if elem % x != r:
                    return -1
        arr = np.array(arr)
        m = np.median(arr)
        total = np.sum(np.abs(arr - m))
        return int(total // x)
sol = Solution()
grid = [[1,5],[2,3]]
x = 1
print(sol.minOperations(grid, x))