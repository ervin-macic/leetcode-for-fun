from typing import List
class Solution:   
    def solveNQueens(self, n: int) -> List[List[str]]:
        # Input: n = 4
        # Output: [[".Q..","...Q","Q...","..Q."],["..Q.","Q...","...Q",".Q.."]]
        ans = []
        col_attacked = [False for _ in range(n)]
        left_diag_attacked = [False for _ in range(2*n)]
        right_diag_attacked = [False for _ in range(2*n)]

        def search(n: int, i: int, sol: List[str], col_attacked, left_diag_attacked, right_diag_attacked):
            nonlocal ans
            # If finished last row
            if i == n:
                ans.append(["".join(row) for row in sol])
                return
            
            # Otherwise continue backtracking ith row
            
            for j in range(n):
                if not col_attacked[j] and not left_diag_attacked[i-j+n-1] and not right_diag_attacked[i+j]:
                    col_attacked[j] = left_diag_attacked[i-j+n-1] = right_diag_attacked[i+j] = True 
                    sol[i][j] = 'Q'
                    search(n, i+1, sol, col_attacked, left_diag_attacked, right_diag_attacked)
                    sol[i][j] = '.'
                    col_attacked[j] = left_diag_attacked[i-j+n-1] = right_diag_attacked[i+j] = False
        
        sol = [['.' for _ in range(n)] for _ in range(n)]
        search(n, 0, sol, col_attacked, left_diag_attacked, right_diag_attacked)
        return ans

sol = Solution()
print(sol.solveNQueens(8))
