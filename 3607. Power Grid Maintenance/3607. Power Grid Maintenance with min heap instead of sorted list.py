from sortedcontainers import SortedList
from collections import defaultdict
import heapq 
class Component:
    def __init__(self):
        self.nodes = []  
    
    def add(self, node):
        heapq.heappush(self.nodes, node)
    
    def get_min_online(self, online):
        while self.nodes and not online[self.nodes[0]]:
            heapq.heappop(self.nodes)
        return self.nodes[0] if self.nodes else -1

class Solution:
    def processQueries(self, c: int, connections: list[list[int]], queries: list[list[int]]) -> list[int]:
        ans = []
        adj = [[] for _ in range(c+1)]
        # Set each node to online initially
        online = {}
        visited = {}
        for node in range(1,c+1):
            online[node] = True
            visited[node] = False

        for edge in connections:
            adj[edge[0]].append(edge[1])
            adj[edge[1]].append(edge[0])
        
        node_to_sl = defaultdict(int)
        def dfs(source, component, idx):
            nonlocal visited
            nonlocal node_to_sl
            component.add(source)
            node_to_sl[source] = idx
            visited[source] = True
            for neighbour in adj[source]:
                if not visited[neighbour]:
                    dfs(neighbour, component, idx)
            return component
        
        idx = 0
        components = []
        for node in range(1,c+1):
            if not visited[node]:
                component = Component()
                component = dfs(node, component, idx)
                components.append(component)
                idx += 1
        
        # Process queries
        for query in queries:
            node = query[1]
            if query[0] == 1:
                if online[node]:
                    # Then node resolves it
                    ans.append(node)
                else:
                    # Find smallest online id node if it exists in node's component
                    component_idx = node_to_sl[node]
                    if components[component_idx]:
                        ans.append(components[component_idx].get_min_online(online))
                    else:
                        ans.append(-1)
            else:
                online[node] = False
        return ans

sol = Solution()
c = 5
connections = [[1,2],[2,3],[3,4],[4,5]]
queries = [[1,3],[2,1],[1,1],[2,2],[1,2]]
print(sol.processQueries(c, connections, queries))