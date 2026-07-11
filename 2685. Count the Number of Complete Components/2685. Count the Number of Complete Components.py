from typing import List 

class Solution:
    def countCompleteComponents(self, n: int, edges: List[List[int]]) -> int:
        adj = [[] for _ in range(n)]
        for a, b in edges:
            adj[a].append(b)
            adj[b].append(a)
        visited = [False] * n

        def dfs(source):
            stack = [source]
            component = []

            while stack:
                node = stack.pop()
                if visited[node]:
                    continue
                visited[node] = True
                component.append(node)
                for nei in adj[node]:
                    if not visited[nei]:
                        stack.append(nei)
            return component
        
        def check_clique(component) -> bool:
            for x in component:
                if len(adj[x]) != len(component) - 1:
                    return False
                for y in component:
                    if x == y: continue 
                    if not adj[x].__contains__(y) or not adj[y].__contains__(x):
                        return False 
            return True 
        ans = 0
        for i in range(n):
            if not visited[i]:
                component = dfs(i)
                ans += check_clique(component)
        return ans

sol = Solution()
n = 6
edges = [[0,1],[0,2],[1,2],[3,4]]
print(sol.countCompleteComponents(n, edges))