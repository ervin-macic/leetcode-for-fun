# Definition for a binary tree node.
from typing import Optional
from collections import deque, defaultdict
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def maxLevelSum(self, root: Optional[TreeNode]) -> int:
        if root == None:
            return 0
        # Do BFS down the tree and collect sums 
        max_level_sum = -1e6
        max_level = 0

        q = deque()
        q.appendleft(root)

        level = 0

        while q:
            level += 1
            level_sum = 0
            for _ in range(len(q)):
                u = q.popleft()
                level_sum += u.val
                if u.left != None:
                    q.append(u.left)
                if u.right != None:
                    q.append(u.right)
                
            if max_level_sum < level_sum:
                max_level_sum = level_sum
                max_level = level
        
        return max_level
            

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


    


sol = Solution()
root = [1,7,0,7,-8,None,None]
root = [1,2,3]
root = build_tree(root)
# 0 -> 1,2
# 1 -> 3,4
# 2 -> 5,6
# i -> 2i+1, 2i+2
print(sol.maxLevelSum(root))
        