from typing import List
from collections import defaultdict
class Solution:
    def countCoveredBuildings(self, n: int, buildings: List[List[int]]) -> int:
        leftmost  = [n+1]*(n+1)
        rightmost = [0]*(n+1)
        upmost    = [0]*(n+1)
        downmost  = [n+1]*(n+1)

        for [i,j] in buildings:
            leftmost[j]  = min(leftmost[j], i)
            rightmost[j] = max(rightmost[j], i)
            downmost[i]  = min(downmost[i], j)
            upmost[i]    = max(upmost[i], j)

        # Count covered buildings
        ans = 0
        for [i,j] in buildings:
            if i > leftmost[j] and i < rightmost[j] and j > downmost[i] and j < upmost[i]:
                ans += 1

        return ans

    
sol = Solution()
n = 3
buildings = [[1,2],[2,2],[3,2],[2,1],[2,3]]
print(sol.countCoveredBuildings(n, buildings))