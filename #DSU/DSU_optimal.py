# This version uses caching. Basically just instantiates the attributes used many times as variables to ease lookup.
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