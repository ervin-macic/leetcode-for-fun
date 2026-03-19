class Solution:
    def numberOfSubmatrices(self, grid: list[list[str]]) -> int:
        total = 0
        m = len(grid)
        n = len(grid[0])
        square_freq = [[(0,0) for _ in range(n+1)] for _ in range(m+1)]
        for i in range(1, m+1):
            for j in range(1, n+1):
                if grid[i-1][j-1] == "X":
                    square_freq[i][j] = (1 + square_freq[i-1][j][0] + square_freq[i][j-1][0] - square_freq[i-1][j-1][0], square_freq[i-1][j][1] + square_freq[i][j-1][1] - square_freq[i-1][j-1][1])
                elif grid[i-1][j-1] == "Y":
                    square_freq[i][j] = (square_freq[i-1][j][0] + square_freq[i][j-1][0] - square_freq[i-1][j-1][0], 1 + square_freq[i-1][j][1] + square_freq[i][j-1][1] - square_freq[i-1][j-1][1])
                else:
                    square_freq[i][j] = (square_freq[i-1][j][0] + square_freq[i][j-1][0] - square_freq[i-1][j-1][0], square_freq[i-1][j][1] + square_freq[i][j-1][1] - square_freq[i-1][j-1][1])
                if square_freq[i][j][0] > 0 and square_freq[i][j][0] == square_freq[i][j][1]:
                    total += 1
        return total
    
sol = Solution()
grid = [["X","Y","."],["Y",".","."]]
print(sol.numberOfSubmatrices(grid))