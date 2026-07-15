from typing import List, Optional
# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def swapPairs(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head or not head.next:
            return head 
        ans = head.next
        prev = head 
        curr = head.next
        toggle = 1
        while curr:
            if toggle:
                remember = curr.next
                curr.next = prev 
                prev.next = remember
                curr = remember
            else:
                if not curr.next:
                    break
                remember = curr.next.next
                curr.next.next = curr 
                prev.next = curr.next 
                curr.next = remember 
                prev = curr
                curr = remember
            toggle = 0
        return ans 
sol = Solution()
head = ListNode(1)
head.next = ListNode(2)
head.next.next = ListNode(3)
# head.next.next.next = ListNode(4)
ans = sol.swapPairs(head)
while ans:
    print(ans.val)
    ans = ans.next 



