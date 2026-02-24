# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from typing import Optional
class Solution:
    def sumRootToLeaf(self, root: Optional[TreeNode]) -> int:
        def dfs(node, prefix):
            if not node:
                return 0
            prefix = (prefix << 1) | node.val
            if not node.left and not node.right:
                return prefix
            return dfs(node.left, prefix) + dfs(node.right, prefix)
        return dfs(root, 0)
sol = Solution()
print(sol.sumRootToLeaf())



