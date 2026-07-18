# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
from collections import defaultdict
from typing import Optional
class Solution:
    def cloneGraph(self, node: Optional[Node]) -> Optional[Node]:
        if not node:
            return Node()
        if len(node.neighbors) == 0:
            return Node(node.val, node.neighbors)
        ans = Node()
        curr = ans
        visited = defaultdict(bool)
        def dfs(node, curr):
            for nei in node.neighbors:
                newNei = Node(nei.val, nei.neighbors)
                curr.neighbors.append(newNei)
                if not visited[nei]:
                    dfs(nei, newNei)
                    visited[node] = True
                
        curr = Node(node.val, node.neighbors)
        visited[node] = True
        dfs(node, curr)
        return ans

sol = Solution()
node1 = Node(1)
node2 = Node(2)
node3 = Node(3)
node4 = Node(4)

# Connect neighbors
node1.neighbors = [node2, node4]
node2.neighbors = [node1, node3]
node3.neighbors = [node2, node4]
node4.neighbors = [node1, node3]

# This is the input to cloneGraph()
graph = node1
newGraph = sol.cloneGraph(node1)
visited = defaultdict(bool)
def dfs(node):
    print(node)
    for nei in node.neighbors:
        if not visited[nei]:
            dfs(nei)

dfs(newGraph)