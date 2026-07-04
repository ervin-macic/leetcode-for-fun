from typing import List
class Solution:
    def minScore(self, n: int, roads: List[List[int]]) -> int:
        minCostEdge = float("inf")
        visited = [False] * (n+1)
        adj = [[] for _ in range(n+1)]
        for a, b, d in roads:
            adj[a].append((b,d))
            adj[b].append((a,d))
        def dfs(node):
            nonlocal minCostEdge
            visited[node] = True 
            for (b, d) in adj[node]:
                minCostEdge = min(minCostEdge, d)
                if not visited[b]:
                    dfs(b)
        dfs(1)
        return minCostEdge
sol = Solution()
n = 4
roads = [[1,2,9],[2,3,6],[2,4,5],[1,4,7]]
print(sol.minScore(n, roads))

            