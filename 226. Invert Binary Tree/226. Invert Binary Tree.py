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
    
from typing import Optional
import math
from collections import deque

def print_bfs(root: Optional[TreeNode]):
    if not root:
        return
    
    q = deque([root])
    while q:
        node = q.popleft()
        print(node.val, end=" ")
        
        if node.left:
            q.append(node.left)
        if node.right:
            q.append(node.right)
class Solution:
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        if root == None:
            return None
        if not root.left and not root.right:
            return root
        right_inverted = self.invertTree(root.right)
        left_inverted = self.invertTree(root.left)
        root.left = right_inverted
        root.right = left_inverted
        return root

sol = Solution()
root = TreeNode.from_list([4,2,7,1,3,6,9])
inverted = sol.invertTree(root)
print_bfs(inverted)
# expected: [4,7,2,9,6,3,1]