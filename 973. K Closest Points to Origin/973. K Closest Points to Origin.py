from typing import List
import heapq 
from math import sqrt
class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        pq = []
        n = len(points)
        if k >= n:
            return points
        for x, y in points:
            d = x*x + y*y
            if len(pq) < k:
                heapq.heappush_max(pq, (d, [x,y]))
            else:
                if pq[0][0] > d:
                    heapq.heapreplace_max(pq, (d, [x,y]))
        return list(map(lambda x: x[1], pq))
sol = Solution()
points = [[3,3],[5,-1],[-2,4]] 
k = 2
print(sol.kClosest(points, k))