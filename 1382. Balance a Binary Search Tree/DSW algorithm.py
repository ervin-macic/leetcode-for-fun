from math import log2, floor, ceil
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def balanceBST(self, root: Optional[TreeNode]) -> Optional[TreeNode]:

        def subtree_height(node):
            if not node:
                return -1
            return 1 + max(subtree_height(node.left), subtree_height(node.right))

        def right_rotate(parent: TreeNode):
            y = parent.right
            if not y or not y.left:
                return
            x = y.left
            b = x.right

            y.left = b
            x.right = y
            parent.right = x

        def left_rotate(parent: TreeNode):
            x = parent.right
            if not x or not x.right:
                return
            y = x.right
            b = y.left

            x.right = b
            y.left = x
            parent.right = y

        vine_head = TreeNode(0)
        vine_head.right = root

        current = vine_head
        while current.right:
            if current.right.left:
                right_rotate(current)
            else:
                current = current.right

        def count_nodes(node):
            count = 0
            while node:
                count += 1
                node = node.right
            return count

        count = count_nodes(vine_head.right)
        
        m = 2 ** floor(log2(count + 1)) - 1

        def make_rotations(vine_head: TreeNode, count: int):
            current = vine_head
            for _ in range(count):
                left_rotate(current)
                current = current.right

        make_rotations(vine_head, count - m)

        while m > 1:
            m //= 2
            make_rotations(vine_head, m)

        return vine_head.right
