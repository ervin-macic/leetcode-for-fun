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

    for vertex in graph.keys():
        if not visited[vertex]:
            dfs(vertex)

    stack.reverse()  # reverse to get topological order
    return stack

graph = {
    1: [2,3,4],
    2: [4],
    3: [2,4],
    4: [],
}

print(topological_sort_dfs(graph))