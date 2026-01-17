from typing import List
class Solution:
    def largestSquareArea(self, bottomLeft: List[List[int]], topRight: List[List[int]]) -> int:
        max_side = 0
        n = len(bottomLeft)
        w, h = 0, 0
        def intersection_dimensions(A, B):
            x_left = max(A[0], B[0])
            y_bottom = max(A[1], B[1])
            x_right = min(A[2], B[2])
            y_top = min(A[3], B[3])

            width = x_right - x_left
            height = y_top - y_bottom

            if width > 0 and height > 0:
                return width, height
            else:
                return 0, 0
            
        for i in range(n):
            a,b = topRight[i]
            x,y = bottomLeft[i]
            for j in range(i + 1, n):
                c,d = bottomLeft[j]
                e,f = topRight[j]
                w, h = intersection_dimensions([x,y,a,b], [c,d,e,f])
                max_side = max(max_side, min(w,h))
        return max_side * max_side 

sol = Solution()
bottomLeft = [[1,1],[2,2],[1,2]]
topRight = [[3,3],[4,4],[3,4]]
print(sol.largestSquareArea(bottomLeft, topRight))