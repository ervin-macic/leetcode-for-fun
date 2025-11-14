class Solution:
    def rangeAddQueries(self, n: int, queries: list[list[int]]) -> list[list[int]]:
        ans = [([0]*n) for _ in range(n)]
        s = [[0]*(n+1) for _ in range(n+1)]
        for q in queries:
            [r1, c1, r2, c2] = q 
            s[r1][c1] += 1
            s[r1][c2+1] -= 1
            s[r2+1][c1] -= 1
            s[r2+1][c2+1] += 1
        for i in range(n):
            for j in range(n):
                is_first_row = (i == 0)
                is_first_col = (j == 0)
                left = (not is_first_row) * ans[i - 1][j]
                top = (not is_first_col) * ans[i][j - 1]
                diag = (not is_first_row) * (not is_first_col) * ans[i - 1][j - 1]
                ans[i][j] = s[i][j] + left + top - diag
        return ans

sol = Solution()
queries = [[1,1,2,2],[0,0,1,1]]
n = 8
queries = [
    [0, 0, 7, 7],   # whole matrix
    [1, 1, 6, 6],
    [2, 2, 5, 5],
    [3, 3, 4, 4],
    [0, 4, 7, 4],   # entire column 4
    [4, 0, 4, 7],   # entire row 4
    [0, 7, 7, 7],   # entire column 7
    [7, 0, 7, 7],   # entire row 7
    [1, 5, 6, 7],
    [3, 0, 6, 3]
]

print(sol.rangeAddQueries(8, queries))

        