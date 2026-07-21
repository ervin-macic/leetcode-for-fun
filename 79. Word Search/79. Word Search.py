from collections import defaultdict
class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        m, n = len(board), len(board[0])
        dirs = [(0,1), (0,-1), (1,0), (-1,0)]
        def dfs(idx, i, j, onPath):
            if idx == len(word):
                return True
            onPath.add((i,j)) 
            possible = False
            for dx, dy in dirs:
                x, y = i + dx, j + dy
                if 0 <= x < m and 0 <= y < n and word[idx] == board[x][y] and (x,y) not in onPath:
                    if dfs(idx+1, x, y, onPath):
                        possible = True
                        break
            onPath.remove((i,j))
            return possible
        
        ans = False
        for i in range(m):
            for j in range(n):
                if board[i][j] == word[0]:
                    onPath = set()
                    idx = 1
                    if dfs(idx, i, j, onPath):
                        return True 
        return False
sol = Solution()
board = [["A","B","C","E"],["S","F","C","S"],["A","D","E","E"]]
word = "ABCCED"
print(sol.exist(board, word))
