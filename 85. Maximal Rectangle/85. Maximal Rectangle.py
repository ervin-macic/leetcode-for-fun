from typing import List
class Solution:
    def maximalRectangle(self, matrix):
        cols = len(matrix[0])
        heights = [0] * cols
        max_area = 0

        for row in matrix:
            for c in range(cols):
                heights[c] = heights[c] + 1 if row[c] == '1' else 0
            stack = []
            for i in range(cols + 1):
                curr = heights[i] if i < cols else 0
                while stack and curr < heights[stack[-1]]:
                    h = heights[stack.pop()]
                    w = i if not stack else i - stack[-1] - 1
                    max_area = max(max_area, h * w)
                stack.append(i)

        return max_area

sol = Solution()
matrix = [["1","0","1","0","0"],["1","0","1","1","1"],["1","1","1","1","1"],["1","0","0","1","0"]]
matrix = [["1","1","1","1","1","1","1","1"],["1","1","1","1","1","1","1","0"],["1","1","1","1","1","1","1","0"],["1","1","1","1","1","0","0","0"],["0","1","1","1","1","0","0","0"]]
print(sol.maximalRectangle(matrix))