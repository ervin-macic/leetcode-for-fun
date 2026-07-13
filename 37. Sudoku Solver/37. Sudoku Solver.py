from typing import List
from dataclasses import dataclass, field
import heapq
@dataclass(order=True) 
class EmptyCell:
    numLegalMoves: int
    legalMoves: List[str] = field(compare=False)
    x: int
    y: int

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
            pq = []
            for i in range(n):
                for j in range(n):
                    if board[i][j] == '.':
                        legalMoves = getLegalMoves(i, j)
                        if not legalMoves:
                            return False
                        emptyCell = EmptyCell(len(legalMoves), legalMoves, i, j)
                        heapq.heappush(pq, emptyCell)
            if not pq:
                return True 
            mostConstrained = heapq.heappop(pq)
            legalMoves, x, y = mostConstrained.legalMoves, mostConstrained.x, mostConstrained.y
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
            
        
        