from typing import List
class Solution:
    def canReach(self, arr: List[int], start: int) -> bool:
        n = len(arr)
        visited = [False] * n
        stack = [start]
        while stack:
            idx = stack.pop()
            if arr[idx] == 0:
                return True
            if not visited[idx]:
                visited[idx] = True
                neighbours = [idx + arr[idx], idx - arr[idx]]
                for neighbour in neighbours:
                    if 0 <= neighbour < n and not visited[neighbour]:
                        stack.append(neighbour)
        return False
sol = Solution()
arr = [4,2,3,0,3,1,2]
start = 5
print(sol.canReach(arr, start))
