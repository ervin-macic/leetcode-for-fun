from typing import List
from collections import defaultdict, Counter
class Solution:
    def minimumHammingDistance(self, source: List[int], target: List[int], allowedSwaps: List[List[int]]) -> int:
        # construct graph from allowed swaps
        # find connected components
        # inside connected components, can get any permutation I want
        # see how set of indices inside the connected components compares with set of indices in target
        # if sets identical, can get 0 added to ans 
        # in general can get best case (size of component - |A cap B|) added to ans
        # keep indices as vertices in graph, compare values 
        n = len(source)
        graph = [[] for i in range(n)]
        visited = defaultdict(bool)
        for a,b in allowedSwaps:
            graph[a].append(b)
            graph[b].append(a)
        
        components = []
        def dfs(node, component) -> List[int]:
            visited[node] = True 
            for neighbour in graph[node]:
                if not visited[neighbour]:
                    component.append(neighbour)
                    dfs(neighbour, component)
            return component
        
        for i in range(n):
            if not visited[i]:
                components.append(dfs(i, [i]))
        
        ans = 0
        for c in components:
            # c is list of indices
            count = Counter()
            for idx in c:
                count[source[idx]] += 1
                count[target[idx]] -= 1
            for v in count.values():
                if v > 0:
                    ans += v
        return ans

sol = Solution()
source = [1,2,3,4]
target = [2,1,4,5]
allowedSwaps = [[0,1],[2,3]]
source = [1,2,3,4]
target = [1,3,2,4]
allowedSwaps = []
source = [5,1,2,4,3]
target = [1,5,4,2,3]
allowedSwaps = [[0,4],[4,2],[1,3],[1,4]]
print(sol.minimumHammingDistance(source, target, allowedSwaps)) 