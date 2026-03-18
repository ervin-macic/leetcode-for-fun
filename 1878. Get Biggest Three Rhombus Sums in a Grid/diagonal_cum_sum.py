from collections import defaultdict
grid = [[3,  4,  5, 1, 3],
        [3,  3,  4, 2, 3],
        [20,30,200,40,10],
        [1,  5,  5, 4, 1],
        [4,  3,  2, 2, 5]]
m = len(grid)
n = len(grid[0])
leftDiagSum = [[0 for _ in range()]]
rightDiagSum = defaultdict(lambda : [0])
for i in range(m):
    for j in range(n):
        leftDiagSum[j-i].append(leftDiagSum[j-i][-1] + grid[i][j])
        rightDiagSum[j+i].append(rightDiagSum[j+i][-1] + grid[i][j])
print(leftDiagSum)
print(rightDiagSum)
# j-i = 0 is main diagonal have length 
# j-i = 1 is one above main diagonal
# j-i = 4 = n-1 is last element

# j-i = -1 ... j-i = -(m-1) is bottom left element
# zelim mapirat dodaj (m-1) svakome onda se n-1 mapira u m+n-2

# j+i = 0 is top left elem
# j+i = 1 is second diagonal
# ... j+i = m+n-2 is bottom right element
