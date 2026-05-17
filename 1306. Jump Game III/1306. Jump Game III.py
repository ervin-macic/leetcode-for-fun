from typing import List
from collections import defaultdict
class Solution:
    def canReach(self, arr: List[int], start: int) -> bool:
        n = len(arr)
        visited = defaultdict(bool)
        def dfs(idx) -> bool:
            visited[idx] = True
            if arr[idx] == 0:
                return True
            candidates = [idx + arr[idx], idx - arr[idx]]
            for neighbour in candidates:
                if 0 <= neighbour < n and not visited[neighbour]:
                    if dfs(neighbour):
                        return True
            return False
        return dfs(start)
sol = Solution()
arr = [4,2,3,0,3,1,2]
start = 5
print(sol.canReach(arr, start))
