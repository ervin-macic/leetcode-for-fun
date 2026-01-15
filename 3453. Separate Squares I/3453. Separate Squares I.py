from typing import List
class Solution:
    def separateSquares(self, squares: List[List[int]]) -> float:
        total_area = 0
        ceiling = 0
        for x, y, side in squares:
            total_area += side * side
            ceiling = max(ceiling, y + side)

        # Do binary search over possible y values
        left = 0.0
        right = ceiling

        while right - left > 1e-5:
            mid = (left + right) / 2
            area = 0.0
            # (Inefficient) Go through all squares and sum total area under y = mid line
            for x, y, side in squares:
                if mid > y:
                    area += side * min(mid - y, side)

            if area >= total_area / 2:
                right = mid
            else:
                left = mid
        # Here certainly right - left <= 1e-5 which is desired tolerance
        # Ends up O(nlogn)
        return right

sol = Solution()
squares = [[0,0,1],[2,2,1]]
print(sol.separateSquares(squares))



