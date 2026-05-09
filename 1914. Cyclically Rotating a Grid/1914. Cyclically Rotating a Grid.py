from typing import List
class Solution:
    def rotateGrid(self, grid: List[List[int]], k: int) -> List[List[int]]:
        m, n = len(grid), len(grid[0])
        for i in range(min(m,n) // 2):
            arr = []
            for j in range(i, n-i-1):
                arr.append(grid[i][j])
            for i1 in range(i, m-i-1):
                arr.append(grid[i1][~i])
            for j in range(n-i-1, i, -1):
                arr.append(grid[~i][j])
            for i1 in range(m-i-1, i, -1):
                arr.append(grid[i1][i])
            print(arr)
            # Fill
            cnt = 0
            s = len(arr)
            for j in range(i, n-i-1):
                grid[i][j] = arr[(cnt + k) % s]
                cnt += 1
            for i1 in range(i, m-i-1):
                grid[i1][~i] = arr[(cnt + k) % s]
                cnt += 1
            for j in range(n-i-1, i, -1):
                grid[~i][j] = arr[(cnt + k) % s]
                cnt += 1
            for i1 in range(m-i-1, i, -1):
                grid[i1][i] = arr[(cnt + k) % s]
                cnt += 1
        return grid 
sol = Solution()
grid = [[1,2,3,4],[5,6,7,8],[9,10,11,12],[13,14,15,16]]
k = 2
print(sol.rotateGrid(grid, k))
            
