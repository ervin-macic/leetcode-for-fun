from typing import List
from collections import defaultdict, Counter
class DSU:
    def __init__(self, n):
        self.p = list(range(n))
        self.sz = [1] * n

    def find(self, x):
        p = self.p
        while p[x] != x:
            p[x] = p[p[x]]   # path halving
            x = p[x]
        return x

    def union(self, a, b):
        p = self.p
        sz = self.sz

        a = self.find(a)
        b = self.find(b)

        if a == b:
            return False

        if sz[a] < sz[b]:
            a, b = b, a

        p[b] = a
        sz[a] += sz[b]
        return True
class Solution:
    def minimumHammingDistance(self, source: List[int], target: List[int], allowedSwaps: List[List[int]]) -> int:
        n = len(source)
        dsu = DSU(n)
        for a,b in allowedSwaps:
            dsu.union(a, b)
        
        ans = 0
        sets = defaultdict(lambda: defaultdict(int))
        for i in range(n):
            root = dsu.find(i)
            sets[root][source[i]] += 1

        for i in range(n):
            root = dsu.find(i)
            if sets[root][target[i]] > 0:
                sets[root][target[i]] -= 1
            else:
                ans += 1
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