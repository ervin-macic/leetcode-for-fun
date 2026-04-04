from typing import List
from dataclasses import dataclass
from bisect import bisect_left, bisect_right

@dataclass
class Robot:
    position: int
    distance: int

class Solution:
    def maxWalls(self, robots: List[int], distance: List[int], walls: List[int]) -> int:
        n = len(robots)
        robots = sorted([Robot(p, d) for p, d in zip(robots, distance)], key=lambda r: r.position)
        walls.sort()

        def count_walls(left, right):
            if left > right:
                return 0
            return bisect_right(walls, right) - bisect_left(walls, left)

        left_count = [0] * n
        right_count = [0] * n

        for i, r in enumerate(robots):
            left_limit = r.position - r.distance
            if i > 0:
                left_limit = max(left_limit, robots[i-1].position + 1)
            left_count[i] = count_walls(left_limit, r.position)

            right_limit = r.position + r.distance
            if i < n - 1:
                right_limit = min(right_limit, robots[i+1].position - 1)
            right_count[i] = count_walls(r.position, right_limit)

        # dp[i][0] = best total walls destroyed if robot i shoots left
        # dp[i][1] = best total walls destroyed if robot i shoots right
        dp = [[0, 0] for _ in range(n)]
        dp[0][0] = left_count[0]
        dp[0][1] = right_count[0]

        for i in range(1, n):
            overlap_left  = max(robots[i].position - robots[i].distance, robots[i-1].position + 1)
            overlap_right = min(robots[i-1].position + robots[i-1].distance, robots[i].position - 1)
            overlap = count_walls(overlap_left, overlap_right)

            dp[i][0] = max(
                dp[i-1][0] + left_count[i],
                dp[i-1][1] + left_count[i] - overlap
            )
            dp[i][1] = max(dp[i-1][0], dp[i-1][1]) + right_count[i]
        return max(dp[n-1])

sol = Solution()
robots = [10,2]
distance = [5,1]
walls = [5,2,7]
robots = [4]
distance = [3]
walls = [1,10]
robots = [11,17,18,32,59,72]
distance = [5,5,10,6,7,2]
walls = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39, 40, 41, 42, 43, 44, 45, 46, 47, 48, 49, 50, 51, 52, 53, 54, 55, 56, 57, 58]
print(sol.maxWalls(robots, distance, walls))