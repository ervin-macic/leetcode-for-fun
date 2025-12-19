from typing import List
from collections import deque
# class UnionFind:
#     def __init__(self, n):
#         self.parent = list(range(n))
#         self.size = [1] * n

#     def find(self, x):
#         if self.parent[x] != x:
#             self.parent[x] = self.find(self.parent[x])
#         return self.parent[x]

#     def union(self, x, y):
#         x = self.find(x)
#         y = self.find(y)

#         if x == y:
#             return False

#         # attach smaller tree to larger tree
#         if self.size[x] < self.size[y]:
#             x, y = y, x

#         self.parent[y] = x
#         self.size[x] += self.size[y]
#         return True

class Solution:
    def findAllPeople(self, n: int, meetings: List[List[int]], firstPerson: int) -> List[int]:
        graph = [[] for _ in range(n)]
        for [x, y, t] in meetings:
            graph[x].append((y,t))
            graph[y].append((x,t))
        first_heard = [10**9+7] * n
        first_heard[0] = 0
        first_heard[firstPerson] = 0
        q = deque()
        q.append((0,0))
        q.append((firstPerson, 0))
        while q:
            (y,t) = q.popleft()
            if t > first_heard[y]: continue
            for (x,t1) in graph[y]:
                if t1 >= t and first_heard[x] > t1:
                    first_heard[x] = t1
                    q.append((x,t1))

        ans = []
        for i in range(n):
            if first_heard[i] != 10**9+7:
                ans.append(i)
        return ans 

sol = Solution()
n = 5
meetings = [[3,4,2],[1,2,1],[2,3,1]]
firstPerson = 1
n = 4
meetings = [[3,1,3],[1,2,2],[0,3,3]]
firstPerson = 3
print(sol.findAllPeople(n, meetings, firstPerson))