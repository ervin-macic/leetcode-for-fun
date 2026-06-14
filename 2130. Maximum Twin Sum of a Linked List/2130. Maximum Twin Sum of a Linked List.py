# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class DoublyLinkedListNode(ListNode):
    def __init__(self, val=0, next=None, prev=None):
        super().__init__()
        self.prev = prev 

class Solution:
    def pairSum(self, head: Optional[ListNode]) -> int:
        curr = DoublyLinkedListNode(head.val, head.next)
        left = curr
        prev = None 
        while curr != None:
            curr.prev = prev
            prev = curr
            if curr.next == None:
                break
            curr = DoublyLinkedListNode(curr.next.val, curr.next.next)
        right = prev
        ans = -1
        while left != None and right != None and left != right.prev:
            ans = max(ans, left.val + right.val)
            left = left.next 
            right = right.prev
        return ans
        