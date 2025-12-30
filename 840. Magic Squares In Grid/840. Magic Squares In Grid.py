from typing import List
from collections import defaultdict
class Solution:
    def numMagicSquaresInside(self, grid: List[List[int]]) -> int:
        row = len(grid)
        col = len(grid[0])
        if row < 3 or col < 3:
            return 0
        ans = 0
        for i in range(row-2):
            for j in range(col-2):
                # Check whether the 3x3 square with top left corner (i,j) is a magic square
                is_magic = True
                if grid[i+1][j+1] != 5 or grid[i][j] % 2 == 1 or grid[i][j+2] % 2 == 1 or grid[i+2][j] % 2 == 1 or grid[i+2][j+2] % 2 == 1:
                    continue
                
                common_sum = 15
                found = [False] * 10
                # Check rows
                for k in range(3):
                    row_sum = 0
                    for l in range(3):
                        row_sum += grid[i+k][j+l]
                        if 1 <= grid[i+k][j+l] <= 9 and not found[grid[i+k][j+l]]:
                            found[grid[i+k][j+l]] = True 
                        else:
                            is_magic = False
                    if row_sum != common_sum:
                        is_magic = False
                        break
                
                if not is_magic:
                    continue
                
                # Check columns:
                for k in range(3):
                    col_sum = 0
                    for l in range(3):
                        col_sum += grid[i+l][j+k]
                    if col_sum != common_sum:
                        is_magic = False
                        break
                
                if not is_magic:
                    continue

                # Check diagonals:
                left_diag_sum = grid[i][j] + grid[i+1][j+1] + grid[i+2][j+2]
                right_diag_sum = grid[i][j+2] + grid[i+1][j+1] + grid[i+2][j]
                print(left_diag_sum, right_diag_sum)
                if left_diag_sum != common_sum or right_diag_sum != common_sum:
                    is_magic = False
                    continue
                
                if is_magic:
                    ans += 1
        return ans


sol = Solution()
grid = [[10,3,5],[1,6,11],[7,9,2]]
print(sol.numMagicSquaresInside(grid))