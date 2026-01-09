from typing import Optional
from collections import defaultdict, deque
# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def subtreeWithAllDeepest(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        def dfs(source) -> (int, TreeNode): # return depth and tree node
            if source == None:
                return (0, source)
            depth_left, node_left = dfs(source.left)
            depth_right, node_right = dfs(source.right)
            if depth_left == depth_right:
                return (depth_left + 1, source)
            elif depth_left > depth_right:
                return (depth_left + 1, node_left)
            else:
                return (depth_right + 1, node_right)
        _, lca = dfs(root)
        return lca

def build_tree(arr):
    if not arr or arr[0] is None:
        return None

    root = TreeNode(arr[0])
    queue = deque([root])
    i = 1

    while queue and i < len(arr):
        node = queue.popleft()

        # left child
        if i < len(arr) and arr[i] is not None:
            node.left = TreeNode(arr[i])
            queue.append(node.left)
        i += 1

        # right child
        if i < len(arr) and arr[i] is not None:
            node.right = TreeNode(arr[i])
            queue.append(node.right)
        i += 1

    return root

root = [3,5,1,6,2,0,8,None,None,7,4]
root = build_tree(root)
sol = Solution()
print(sol.subtreeWithAllDeepest(root))
