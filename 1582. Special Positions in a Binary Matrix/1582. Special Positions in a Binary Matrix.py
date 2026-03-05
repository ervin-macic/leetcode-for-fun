class Solution:
    def numSpecial(self, mat: list[list[int]]) -> int:
        m = len(mat)
        n = len(mat[0])
        ones_seen_row = [0 for _ in range(m)]
        ones_seen_col = [0 for _ in range(n)]
        for i in range(m):
            for j in range(n):
                ones_seen_col[j] += mat[i][j]
                ones_seen_row[i] += mat[i][j]
        total = 0
        for i in range(m):
            if ones_seen_row[i] == 1:
                for j in range(n):
                    if mat[i][j] == 1 and ones_seen_col[j] == 1:
                        total += 1 
        return total 