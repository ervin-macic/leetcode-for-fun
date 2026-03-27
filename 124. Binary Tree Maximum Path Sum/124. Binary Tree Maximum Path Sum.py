# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
from typing import Optional
from collections import defaultdict, deque
class Solution:
    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        
        ans = root.val
        l = defaultdict(int)
        r = defaultdict(int)
        
        def dfs(current: TreeNode):
            nonlocal ans
            if current is None: return 0
            left, right = current.left, current.right
            leftVal = max(0, dfs(left))
            rightVal = max(0, dfs(right))
            ans = max(ans, leftVal + current.val + rightVal)
            return current.val + max(leftVal, rightVal)
        dfs(root)
        return ans
    
root = TreeNode(-10)
root.left = TreeNode(9)
root.right = TreeNode(20)
root.right.left = TreeNode(15)
root.right.right = TreeNode(7)
sol = Solution()
print(sol.maxPathSum(root))