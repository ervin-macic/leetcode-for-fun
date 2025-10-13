import heapq
from collections import defaultdict
def dijkstra(graph, source) -> list[int]:
    distance = {node: float('inf') for node in graph}
    distance[source] = 0
    pq = [] # min-priority queue
    heapq.heappush(pq, (0, source)) # (key distance, value is node)
    while pq:
        cur_distance, u = heapq.heappop(pq)
        if cur_distance > dist[u]: # if processed skip him
            continue

        for v, w in graph[u]:
            if distance[u] + w < distance[v]:
                distance[v] = distance[u] + w 
                heapq.heappush(pq, (dist[v], v))

    return distance

def main():
    V = int(input("Number of vertices: "))
    E = int(input("Number of edges: "))
    graph = defaultdict(list)
    visited = [False] * V
    for i in range(E):
        u, v, w = map(int, input(f"Input {i}th edge: ").split())
        graph[u].append((v,w))
        graph[v].append((u,w))
    
    
    distance = dijkstra(graph, 0)
    for i in range(len(distance)):
        print(f"{i}: {distance[i]}")

main()