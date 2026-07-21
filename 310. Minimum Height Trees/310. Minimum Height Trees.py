from collections import deque
class Solution:
    def findMinHeightTrees(self, n: int, edges: List[List[int]]) -> List[int]:
        if n == 1:
            return [0]
        graph = [[] for _ in range(n)]
        for a,b in edges:
            graph[a].append(b)
            graph[b].append(a)

        # bfs once to find most distant node from anywhere
        q = deque()
        visited = [False] * n 
        q.append(0)
        dist = {}
        maxDist = 0
        maxDistNode = None
        dist[0] = 0
        while q:
            node = q.pop()
            visited[node] = True
            for nei in graph[node]:
                if not visited[nei]:
                    q.append(nei)
                    visited[nei] = True 
                    dist[nei] = dist[node] + 1
                    if dist[nei] > maxDist:
                        maxDistNode = nei
                        maxDist = dist[nei]
        # run bfs from maxDistNode and get length of diameter
        q = deque()
        dist = {}
        source = maxDistNode
        q.append(source)
        maxDist = 0
        maxDistNode = None
        visited = [False] * n 
        dist[source] = 0
        parent = [None] * n
        while q:
            node = q.popleft()
            visited[node] = True
            for nei in graph[node]:
                if not visited[nei]:
                    q.append(nei)
                    visited[nei] = True 
                    parent[nei] = node
                    dist[nei] = dist[node] + 1
                    if dist[nei] > maxDist:
                        maxDistNode = nei
                        maxDist = dist[nei]
        curr = maxDistNode
        for i in range(maxDist // 2):
            curr = parent[curr]
        if maxDist % 2 == 0:
            # just return middle of diameter
            return [curr]
        # return two middle nodes of diameter
        return [curr, parent[curr]]
sol = Solution()
n = 6
edges = [[3,0],[3,1],[3,2],[3,4],[5,4]]
print(sol.findMinHeightTrees(n, edges))

    
                    