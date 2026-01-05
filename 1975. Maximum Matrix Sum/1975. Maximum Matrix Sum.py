from typing import List
import math
class Solution:
    def maxMatrixSum(self, matrix: List[List[int]]) -> int:
        ans = 0
        num_neg = 0
        min_abs = 10**9+7
        for row in matrix:
            for x in row:
                y = abs(x)
                ans += y
                if y < min_abs:
                    min_abs = y
                if x < 0:
                    num_neg += 1
        if num_neg % 2 == 0:
            return ans 
        return ans - 2 * min_abs
sol = Solution()
matrix = [[1,2,3],[-1,-2,-3],[1,2,3]]
matrix = [[1,-1],[-1,1]]
print(sol.maxMatrixSum(matrix))

        