# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        curr = head
        sz = 0
        while curr:
            sz += 1
            curr = curr.next 
        if n == 1 and sz == 1:
            return None
        curr = head 
        i = 0
        prev = None
        while i < sz and curr:
            if i == sz - n:
                if prev:
                    prev.next = curr.next
                    return head
                else:
                    return head.next
            prev = curr 
            curr = curr.next 
            i += 1
        return None
        