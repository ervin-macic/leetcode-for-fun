from collections import defaultdict

edges = [(0, 1), (1, 2), (2, 0), (3, 4)]
V = 0
for e in edges:
    V = max(V, max(e[0], e[1]))

graph = [[] for _ in range(V+1)]

for e in edges:
    graph[e[0]].append(e[1])
    graph[e[1]].append(e[0])

visited = defaultdict(bool)
def dfs(node):
    visited[node] = True

    for neighbor in graph[node]:
        if not visited[neighbor]:
            dfs(neighbor)

num_components = 0

for node in range(V+1):
    if not visited[node]:
        num_components += 1
        dfs(node)

print(num_components)
