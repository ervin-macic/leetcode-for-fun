from typing import Optional
# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        def dfs(node):
            if not node:
                return 0
            left_height = dfs(node.left)
            if left_height == -1: 
                return -1
            right_height = dfs(node.right)
            if right_height == -1: 
                return -1
            if abs(left_height - right_height) > 1:
                return -1
            return 1 + max(left_height, right_height)
        return dfs(root) != -1
    
sol = Solution()
root = [3,9,20,None,None,15,7]
print(sol.isBalanced(root))
            
            
        