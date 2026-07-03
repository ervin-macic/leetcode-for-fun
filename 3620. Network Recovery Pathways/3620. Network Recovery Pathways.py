from bisect import bisect_left
from typing import List
import heapq
class Solution:
    def findMaxPathScore(self, edges: List[List[int]], online: List[bool], k: int) -> int:
        n = len(online)
        adj = [[] for _ in range(n)]
        maxEdge = -1
        for [u, v, c] in edges:
            adj[u].append((c, v))
            maxEdge = max(maxEdge, c)

        def f(threshold):
            q = []
            heapq.heappush(q, (0, 0))
            d = [float("inf") for _ in range(n)]
            d[0] = 0
            while q:
                dist, u = heapq.heappop(q)
                # stale entry check
                if dist != d[u]:
                    continue

                for (c, v) in adj[u]:
                    if online[v] and c >= threshold:
                        # frontier updating
                        if d[u] + c < d[v]:
                            d[v] = d[u] + c
                            heapq.heappush(q, (d[v], v))
            return d[n-1] <= k 
        # search space is of form True True ... True False False .. False
        return bisect_left(range(maxEdge+1), True, key=lambda x: f(x) == False) - 1

sol = Solution()
edges = [[0,1,7],[1,4,5],[0,2,6],[2,3,6],[3,4,2],[2,4,6]]
online = [True,True,True,False,True]
k = 12
print(sol.findMaxPathScore(edges, online, k))