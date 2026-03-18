grid = [[7,2,9],
        [1,5,0],
        [2,6,6]]
m = len(grid)
n = len(grid[0])
k = 20
square_sum = [[0 for _ in range(m+1)] for _ in range(n+1)]
for i in range(1, m+1):
    for j in range(1, n+1):
        square_sum[i][j] = grid[i-1][j-1] + square_sum[i-1][j] + square_sum[i][j-1] - square_sum[i-1][j-1]

print(square_sum)