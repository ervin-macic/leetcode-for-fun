from typing import List
class Solution:
    def separateSquares(self, squares: List[List[int]]) -> float:
        total_area = 0
        ceiling = 0
        for x, y, side in squares:
            total_area += side * side
            ceiling = max(ceiling, y + side)

        left = 0.0
        right = ceiling

        while right - left > 1e-5:
            mid = (left + right) / 2
            area = 0.0
            for x, y, side in squares:
                if mid > y:
                    area += side * min(mid - y, side)

            if area >= total_area / 2:
                right = mid
            else:
                left = mid

        return right

sol = Solution()
squares = [[0,0,1],[2,2,1]]
print(sol.separateSquares(squares))



