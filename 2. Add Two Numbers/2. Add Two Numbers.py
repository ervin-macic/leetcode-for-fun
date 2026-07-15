from typing import List, Optional
# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        ans = ListNode()
        carry = 0
        curr = ans
        while l1 or l2 or carry:
            a = l1.val if l1 else 0
            b = l2.val if l2 else 0
            curr.next = ListNode((a+b+carry) % 10)
            curr = curr.next

            carry = 1 if a+b+carry > 9 else 0
            if l1:
                l1 = l1.next 
            if l2:
                l2 = l2.next 
        return ans.next
    
sol = Solution()
# 342 + 465 = 807
l1 = ListNode(2, ListNode(4, ListNode(3)))
l2 = ListNode(5, ListNode(6, ListNode(4)))
# 99 + 1 = 100
l1 = ListNode(9, ListNode(9))
l2 = ListNode(1)

ans = sol.addTwoNumbers(l1, l2)
while ans:
    print(ans.val)
    ans = ans.next