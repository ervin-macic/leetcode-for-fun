from typing import Optional
from collections import deque, defaultdict

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def maxProduct(self, root: Optional[TreeNode]) -> int:
        MOD = 1000000007
        if root == None:
            return 0
        
        # Get total sum in one pass
        total = 0
        def dfs(source):
            nonlocal total
            total += source.val
            if source.left != None:
                dfs(source.left)
            if source.right != None:
                dfs(source.right)
        dfs(root)

        # Find sum of each subtree
        best_product = 0
        
        def subtree_sum(source):
            nonlocal best_product
            current_sum = 0
            if source.left is None and source.right is None:
                current_sum = source.val
            else:
                left_sum = 0
                right_sum = 0
                if source.left is not None:
                    left_sum = subtree_sum(source.left)
                if source.right is not None:
                    right_sum = subtree_sum(source.right)
                
                current_sum = left_sum + source.val + right_sum
            best_product = max(best_product, current_sum * (total - current_sum))
            return current_sum
            
        subtree_sum(root)
        return best_product % MOD
            

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
root = [1,None,2,3,4,None,None,5,6]
root = [1,1]
root = build_tree(root)
# 0 -> 1,2
# 1 -> 3,4
# 2 -> 5,6
# i -> 2i+1, 2i+2
print(sol.maxProduct(root))
        