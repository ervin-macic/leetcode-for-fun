from collections import defaultdict
def find_SCCs(graph):
    n = len(graph)
    time = 1
    visited = defaultdict(bool)
    f = [(-1,-1)] * n

    # Get finshing times using DFS
    def dfs(graph, source):
        nonlocal visited, time, f
        visited[source] = True
        time += 1
        for neighbour in graph[source]:
            if not visited[neighbour]:
                dfs(graph, neighbour)
        f[source] = (time, source)
        time += 1

    for node in range(n):
        if not visited[node]:
            dfs(graph, node)

    # SCC search
    f = sorted(f, reverse=True)

    # Construct transpose of graph
    graph_T = [[] for _ in range(n)] 
    for node in range(n):
        for neighbour in graph[node]:
            graph_T[neighbour].append(node)
    
    # Call DFS on nodes in decreasing order of finishing time on transposed graph
    visited = defaultdict(bool)
    def scc_dfs(node, component):
        nonlocal graph_T, visited
        visited[node] = True 
        component.append(node)
        for neighbour in graph_T[node]:
            if not visited[neighbour]:
                component = scc_dfs(neighbour, component)
        return component 
    SCCs = []
    for (finishing_time, node) in f:
        if not visited[node]:
            SCCs.append(scc_dfs(node, []))
    return SCCs
    
graph = [[], [2,6], [3,7], [4,8], [5,8,9], [10], [7], [1,8], [3], [10], [5]]
print(find_SCCs(graph))
