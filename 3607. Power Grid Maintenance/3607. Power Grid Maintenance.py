from sortedcontainers import SortedList
from collections import defaultdict

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
                component = SortedList()
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
                    '''found_online_node = False 
                    for n in components[component_idx]:
                        if online[n]:
                            ans.append(n)
                            found_online_node = True
                            break 
                    if not found_online_node:
                        ans.append(-1)''' 
                    if components[component_idx]:
                        ans.append(components[component_idx][0])
                    else:
                        ans.append(-1)
            else:
                component_idx = node_to_sl[node]
                if online[node] and components[component_idx]:
                    components[component_idx].remove(node)
                online[node] = False
        return ans

sol = Solution()
c = 5
connections = [[1,2],[2,3],[3,4],[4,5]]
queries = [[1,3],[2,1],[1,1],[2,2],[1,2]]
print(sol.processQueries(c, connections, queries))