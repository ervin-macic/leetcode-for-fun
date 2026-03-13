class Solution(object):
    def maxStability(self, n, edges, k):
        spanning_tree = []
        parent = [0 for _ in range(n)]
        height = [0 for _ in range(n)]

        def make_set(x: int):
            parent[x] = x

        # return root of x and do path compression along the way
        def root(x):
            if x != parent[x]:
                parent[x] = root(parent[x])
            return parent[x] 
        
        # make ry the parent of rx (attach rx subtree as a new subtree of ry)
        def link(rx, ry):
            parent[rx] = ry
        
        def union(x, y):
            rx = root(x)
            ry = root(y)
            if rx == ry:
                return
            if height[rx] < height[ry]:
                link(rx,ry)
            elif height[rx] > height[ry]:
                link(ry, rx)
            else:
                link(rx, ry)
                height[ry] += 1
        
        for i in range(n):
            make_set(i)
        
        edges_added = 0
        for [u, v, s, must] in edges:
            if must == 1:
                if root(u) == root(v):
                    return -1
                spanning_tree.append([u,v,s,must])
                union(u, v)
        
        edges.sort(key = lambda lst: -lst[2])

        i = 0
        while len(spanning_tree) != n-1 and i < len(edges):
            u,v,s,must = edges[i]
            if must == 0:
                if root(u) != root(v):
                    spanning_tree.append([u,v,s,must])
                    union(u,v)
            i += 1

        if len(spanning_tree) != n-1:
            return -1
        
        spanning_tree.sort(key = lambda lst: lst[2])

        # use k moves on k smallest non-must edges
        i = 0
        while i < len(spanning_tree) and k > 0:
            [u,v,s,must] = spanning_tree[i]
            if must == 0:
                spanning_tree[i][2] *= 2
                k -= 1
            i += 1
        
        # get min edge value 
        mini = float("inf")
        for [_,_,s,_] in spanning_tree:
            if mini > s:
                mini = s 
        return mini

sol = Solution()
n = 3
edges = [[0,1,4,0],[1,2,3,0],[0,2,1,0]]
k = 2
n = 3
edges = [[0,1,1,1],[1,2,1,1],[2,0,1,1]]
k = 0
print(sol.maxStability(n, edges, k))