from collections import defaultdict
from typing import List, Optional

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def createBinaryTree(self, descriptions: List[List[int]]) -> Optional[TreeNode]:
        if len(descriptions) == 0:
            return None 
        
        # change data structure
        nodeMap = {}
        children = set()
        for [parent, child, isLeft] in descriptions:
            if parent not in nodeMap:
                nodeMap[parent] = TreeNode(parent)
            if child not in nodeMap:
                nodeMap[child] = TreeNode(child)
            children.add(child)
            if isLeft:
                nodeMap[parent].left = nodeMap[child]
            else:
                nodeMap[parent].right = nodeMap[child]
        
        for node in nodeMap.values():
            if node.val not in children:
                return node 
            
            

sol = Solution()
descriptions = [[20,15,1],[20,17,0],[50,20,1],[50,80,0],[80,19,1]]
root = sol.createBinaryTree(descriptions)
print(root.val)
left = root.left 
print(left.val)
right = root.right
print(right.val)