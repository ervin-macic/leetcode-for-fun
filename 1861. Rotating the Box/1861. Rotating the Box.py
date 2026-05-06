from typing import List 
class Solution:
    def rotateTheBox(self, boxGrid: List[List[str]]) -> List[List[str]]:
        m, n = len(boxGrid), len(boxGrid[0])
        rotatedGrid = [['.' for _ in range(m)] for _ in range(n)]
        for i in range(m):
            j = 0
            while j < n:
                cnt = 0
                while j < n and boxGrid[i][j] != '*':
                    cnt += (boxGrid[i][j] == '#')
                    j += 1
                i1 = j-1
                j1 = ~i
                while cnt > 0:
                    rotatedGrid[i1][j1] = '#'
                    cnt -= 1
                    i1 -= 1
                if j != n:
                    rotatedGrid[j][j1] = '*'
                j += 1
        return rotatedGrid
sol = Solution()
boxGrid = [["#","#","*",".","*","."],
              ["#","#","#","*",".","."],
              ["#","#","#",".","#","."]]
print(sol.rotateTheBox(boxGrid))
                

