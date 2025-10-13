from collections import deque

def dfs(graph, visited, source):
    print(source)
    visited[source] = True 
    for neighbor in graph[source]:
        if not visited[neighbor]:
            dfs(graph, visited, neighbor)

def bfs(graph, visited, distance, source):
    q = deque()
    q.append(source)
    distance[source] = 0
    visited[source] = True
    while q:
        u = q.popleft()
        print(u)
        for neighbor in graph[u]:
            if not visited[neighbor]:
                visited[neighbor] = True
                q.append(neighbor)
                distance[neighbor] = distance[u] + 1


def main():
    V = int(input("Number of vertices: "))
    E = int(input("Number of edges: "))
    graph = [[] for _ in range(V)]
    visited = [False] * V
    for i in range(E):
        u, v = map(int, input(f"Input {i}th edge: ").split())
        graph[u].append(v)
        graph[v].append(u)
    
    for v in range(V):
        if not visited[v]:
            dfs(graph, visited, v)
    
    visited = [False] * V
    distances = [-1] * V
    bfs(graph, visited, distances, 0)

    for i, d in enumerate(distances):
        print(f"{i}: {d}")

main()
