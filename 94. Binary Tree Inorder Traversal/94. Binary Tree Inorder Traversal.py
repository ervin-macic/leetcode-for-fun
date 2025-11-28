# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
    @classmethod
    def from_list(cls, arr):
        """Build a binary tree from a list (typical LeetCode format)."""
        if not arr:
            return None

        nodes = [None if x is None else cls(x) for x in arr]
        kids = nodes[::-1]

        root = kids.pop()

        for node in nodes:
            if node:
                if kids:
                    node.left = kids.pop()
                if kids:
                    node.right = kids.pop()
        return root
    
from typing import List, Optional
class Solution:
    def inorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        if not root:
            return []
        if not root.left and not root.right:
            return [root.val]
        if not root.left:
            return [root.val] + self.inorderTraversal(root.right)
        left_traversal = self.inorderTraversal(root.left)
        right_traversal = self.inorderTraversal(root.right)
        return left_traversal + [root.val] + right_traversal

sol = Solution()
root = TreeNode.from_list([1,2,3,4,5,None,8,None,None,6,7,9])
print(sol.inorderTraversal(root))