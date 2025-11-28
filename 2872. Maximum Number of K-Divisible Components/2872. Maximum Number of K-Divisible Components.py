from typing import List 
from collections import defaultdict
class Solution:
    def maxKDivisibleComponents(self, n: int, edges: List[List[int]], values: List[int], k: int) -> int:
        if sum(values) % k != 0:
            return -1
        ans = 0
        graph = [[] for _ in range(n)]
        for [u,v] in edges:
            graph[u].append(v)
            graph[v].append(u)
        visited = defaultdict(bool)

        def dfs(graph, source) -> int:
            nonlocal ans
            visited[source] = True
            total = values[source]
            for neighbour in graph[source]:
                if not visited[neighbour]:
                    total += dfs(graph, neighbour)
            if total % k == 0:
                ans += 1
                return 0
            return total
        for node in range(n):
            if not visited[node]:
                dfs(graph, node)
        return ans

sol = Solution()
n = 5
edges = [[0,2],[1,2],[1,3],[2,4]]
values = [1,8,1,4,4]
k = 6
n = 7
edges = [[0,1],[0,2],[1,3],[1,4],[2,5],[2,6]]
values = [3,0,6,1,5,2,1]
k = 3
print(sol.maxKDivisibleComponents(n, edges, values, k))