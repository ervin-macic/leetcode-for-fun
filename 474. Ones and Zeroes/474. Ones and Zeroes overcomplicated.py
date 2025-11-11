from collections import defaultdict
def topological_sort_dfs(graph):
        visited = defaultdict(bool)
        stack = []

        def dfs(v):
            visited[v] = True
            for neighbor in graph[v]:
                if not visited[neighbor]:
                    dfs(neighbor)
            stack.append(v) 

        for vertex in list(graph.keys()):
            if not visited[vertex]:
                dfs(vertex)

        stack.reverse()  # reverse to get topological order
        return stack
def remove_first_value(lst, value):
        try:
            i = lst.index(value)
            return lst[:i] + lst[i+1:]
        except ValueError:
            return lst[:]
def dp(graph, hasse, m: int, n: int, ans: int) -> int:
    if len(hasse) == 0: return 0
    # Traverse and DP on Hasse
    top_nodes = [hasse[0]]
    for i in range(1, len(hasse)):
        if (hasse[i][0] >= hasse[i-1][0] and hasse[i][1] >= hasse[i-1][1]):
            break
        else:
            top_nodes.append(hasse[i])
    for node in top_nodes:
        if m < node[0] or n < node[1]:
            continue
        else:
            # print(f"In DP, considering top value: {node}")
            ans += 1
            # print(f"..with ans: {ans}")
            new_m = m - node[0]
            new_n = n - node[1]
            new_hasse = remove_first_value(hasse, node)
            ans = max(dp(graph, new_hasse, new_m, new_n, ans), ans)
    return ans

class Solution:
    def findMaxForm(self, strs: list[str], m: int, n: int) -> int:
        N = len(strs)
        # Construct pairs
        pairs = []
        for s in strs:
            pairs.append((s.count('0'), s.count('1')))

        ans = 0
        # Construct graph ordering on pairs
        graph = defaultdict(list)
        for i in range(N):
            for j in range(N):
                if pairs[i][0] <= pairs[j][0] and pairs[i][1] <= pairs[j][1]:
                    graph[pairs[i]].append(pairs[j])
        
        # Construct Hasse diagram
        hasse = topological_sort_dfs(graph)

        # Traverse and DP on Hasse
        print(len(hasse))
        print(len(strs))
        top_nodes = [hasse[0]]
        for i in range(1, N):
            if (hasse[i][0] >= hasse[i-1][0] and hasse[i][1] >= hasse[i-1][1]):
                break
            else:
                top_nodes.append(hasse[i])

        for node in top_nodes:
            if m < node[0] or n < node[1]:
                continue
            else:
                # print(f"Considering: {node} as top value")
                ans = 1
                new_m = m - node[0]
                new_n = n - node[1]
                new_hasse = remove_first_value(hasse, node)
                ans = max(dp(graph, new_hasse, new_m, new_n, ans), ans)
        return ans

sol = Solution()
strs = ["10","0001","111001","1","0"]
m = 5
n = 3
strs = ["00011","00001","00001","0011","111"]
m = 8
n = 5
print(sol.findMaxForm(strs, m, n))