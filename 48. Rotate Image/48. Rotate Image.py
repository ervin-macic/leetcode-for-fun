from typing import List
class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        n = len(matrix)
        for i in range(n):
            for j in range(i, n - i - 1):
                a, b, c, d = matrix[i][j], matrix[j][n-1-i], matrix[n-1-i][n-1-j], matrix[n-1-j][i]
                matrix[i][j], matrix[j][n-1-i], matrix[n-1-i][n-1-j], matrix[n-1-j][i] = d, a, b, c 
sol = Solution()
matrix = [[5,1,9,11],[2,4,8,10],[13,3,6,7],[15,14,12,16]]
sol.rotate(matrix)