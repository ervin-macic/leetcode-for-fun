# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
from typing import List, Optional
class Solution:
    def balanceBST(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        
        lst = []
        def dfs(node):
            if not node:
                return
            dfs(node.left)
            lst.append(node.val)
            dfs(node.right)
        
        def build_bst(lst: List[int]) -> TreeNode:
            n = len(lst)
            if n == 0:
                return 
            if n == 1:
                return TreeNode(lst[0])
            return TreeNode(lst[n // 2], build_bst(lst[:(n//2)]), build_bst(lst[(n // 2) + 1:]))
        dfs(root)
        return build_bst(lst)
        

        