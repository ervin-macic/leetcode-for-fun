class Solution:
    def largestSubmatrix(self, matrix: list[list[int]]) -> int:
        m = len(matrix)
        n = len(matrix[0])
        ones = [[0 for _ in range(n)] for _ in range(m)]
        for j in range(n):
            for i in range(m):
                if matrix[i][j] == 1:
                    if i == 0:
                        ones[i][j] = 1
                    else:
                        ones[i][j] = ones[i-1][j] + 1
        ans = 0
        for i in range(m):
            ones_row_i_sorted = sorted(ones[i])
            for j in range(n):
                ans = max(ans, (n-j) * ones_row_i_sorted[j])
        return ans

sol = Solution()
matrix = [[0,0,1],
          [1,1,1],
          [1,0,1]]
print(sol.largestSubmatrix(matrix))