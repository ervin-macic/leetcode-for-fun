from collections import defaultdict
from typing import Optional
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def modifiedList(self, nums: list[int], head: Optional[ListNode]) -> Optional[ListNode]:
        previous = None 
        current = head 
        d = defaultdict(bool)
        for num in nums:
            d[num] = True 
        while current:
            removed = False
            if d[current.val]:
                if previous == None:
                    head = head.next
                    removed = True
                else:
                    previous.next = current.next
                    removed = True 
            if not removed:
                previous = current
            current = current.next
        return head

        

sol = Solution()
nums1 = [1,2,3]
vals = [1, 2, 3, 4,5]
head = None
for num in reversed(vals):
    head = ListNode(num, head)

ptr = sol.modifiedList(nums1, head)
while ptr:
    print(ptr.val)
    ptr = ptr.next
