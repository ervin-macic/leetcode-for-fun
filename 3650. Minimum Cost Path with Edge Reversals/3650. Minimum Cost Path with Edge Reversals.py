from collections import defaultdict
from typing import List
import heapq
class Solution:
    def minCost(self, n: int, edges: List[List[int]]) -> int:
        graph = [[] for _ in range(n)]
        for (u,v,w) in edges:
            graph[u].append((v,w))
            graph[v].append((u,2*w))
                
        q = []
        visited = defaultdict(bool)
        d = defaultdict(lambda: 10**9+7)
        heapq.heappush(q, (0, 0))
        d[0] = 0
        while q:
            dist, u = heapq.heappop(q)
            if dist > d[u]:
                continue

            for v, w in graph[u]:
                if d[v] > d[u] + w:
                    d[v] = d[u] + w
                    heapq.heappush(q, (d[v], v))

        if d[n-1] == 10**9+7:
            return -1 
        return d[n-1]
    
sol = Solution()
n = 4
edges = [[0,1,3],[3,1,1],[2,3,4],[0,2,2]]
print(sol.minCost(n, edges))