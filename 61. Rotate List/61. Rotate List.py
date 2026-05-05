# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
from typing import Optional
class Solution:
    def rotateRight(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        if head == None:
            return None
        curr = head
        n = 1
        while curr.next != None:
            curr = curr.next
            n += 1
        k %= n
        # curr is last node 
        curr.next = head 
        curr = head 
        i = 0
        while i != (n-1-k):
            curr = curr.next
            i += 1
        # curr is (n-1-k)th node
        head = curr.next 
        curr.next = None
        return head

head = ListNode(1, ListNode(2, ListNode(3, ListNode(4, ListNode(5)))))
sol = Solution()
k = 2
head = sol.rotateRight(head, k)
curr = head 
while curr != None:
    print(curr.val)
    curr = curr.next
        