from typing import List
class Solution:
    def maximalRectangle(self, matrix: List[List[str]]) -> int:
        rows, cols = len(matrix), len(matrix[0])
        
        maxArea = 0
        for i in range(rows):
            height = [0] * cols 
            for j in range(cols):
                if matrix[i][j] == '1':
                    height[j] += 1
            for i in range(cols + 1):
                stack = []
                while stack and i < cols:
            maxArea = max(maxArea, h*w)
        return maxArea
sol = Solution()
matrix = [["1","0","1","0","0"],["1","0","1","1","1"],["1","1","1","1","1"],["1","0","0","1","0"]]
print(sol.maximalRectangle(matrix))