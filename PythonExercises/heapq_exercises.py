import heapq 

h = [3,5,1,6,4,7]
heapq.heapify(h)
print(h)
heapq.heappush(h, 10)
print(h)
heapq.heappop(h)
print(h)