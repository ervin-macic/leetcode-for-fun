from typing import List

class Solution:
    def solveSudoku(self, board: List[List[str]]) -> None:
        n = len(board) # = 9 always
        def getLegalMoves(x, y) -> List[str]:
            assert (0 <= x < n and 0 <= y < n and board[x][y] == '.')
            illegal = set()
            # check column
            for j in range(n):
                if j != y and board[x][j] != '.':
                    illegal.add(board[x][j])
            # check row
            for i in range(n):
                if i != x and board[i][y] != '.':
                    illegal.add(board[i][y])
            # check 3x3s
            for i in range(3*(x//3), 3*(x//3)+3):
                for j in range(3*(y//3), 3*(y//3)+3):
                    if i == x and j == y: continue 
                    if board[i][j] != '.':
                        illegal.add(board[i][j])
            legal = []
            for k in range(1, 10):
                if str(k) not in illegal:
                    legal.append(str(k))
            return legal
        
        def solve() -> bool:
            # most constrained empty cells first
            mostConstrained = None
            minMoves = 10
            for i in range(n):
                for j in range(n):
                    if board[i][j] == '.':
                        legalMoves = getLegalMoves(i, j)
                        if not legalMoves:
                            return False
                        if len(legalMoves) < minMoves:
                            minMoves = len(legalMoves)
                            mostConstrained = ((i, j), legalMoves)
            if not mostConstrained:
                return True 
            (x, y), legalMoves = mostConstrained
            for move in legalMoves:
                board[x][y] = move
                if solve():
                    return True
                else:
                    board[x][y] = '.'
            return False 
        solve()

sol = Solution()
board = [["5","3",".",".","7",".",".",".","."],
         ["6",".",".","1","9","5",".",".","."],
         [".","9","8",".",".",".",".","6","."],
         ["8",".",".",".","6",".",".",".","3"],
         ["4",".",".","8",".","3",".",".","1"],
         ["7",".",".",".","2",".",".",".","6"],
         [".","6",".",".",".",".","2","8","."],
         [".",".",".","4","1","9",".",".","5"],
         [".",".",".",".","8",".",".","7","9"]]
print(sol.solveSudoku(board))
print(board)
            
        
        