from collections import defaultdict
from typing import List 
class Solution:
    def assignEdgeWeights(self, edges: List[List[int]]) -> int:
        MOD = 10**9+7
        n = len(edges) + 1
        adj = [[] for _ in range(n+1)]
        for u,v in edges:
            adj[u].append(v)
            adj[v].append(u)
        
        maxDepth = 0
        def dfs(node, parent, depth):
            nonlocal maxDepth
            maxDepth = max(maxDepth, depth)
            for neighbour in adj[node]:
                if neighbour != parent:
                    dfs(neighbour, node, depth+1)

        root = 1
        dfs(root, 0, 0)
        return pow(2, maxDepth-1, MOD)
    
sol = Solution()
edges = [[1,2],[1,3],[3,4],[3,5]]
print(sol.assignEdgeWeights(edges))