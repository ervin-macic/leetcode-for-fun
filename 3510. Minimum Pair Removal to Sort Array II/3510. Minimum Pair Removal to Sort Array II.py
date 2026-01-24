from typing import List
from sortedcontainers import SortedList
from collections import defaultdict
class LinkedList:
    def __init__(self, val = None, prev = None, next = None):
        self.val = val
        self.prev = prev 
        self.next = next
class Solution:
    def minimumPairRemoval(self, nums: List[int]) -> int:
        n = len(nums)
        # Hold list as linked list
        head = LinkedList(nums[0])
        curr = head
        for i in range(1, n):
            node = LinkedList(nums[i], curr)
            curr.next = node 
            curr = node
        curr = head

        # Hold sums a[i] + a[i+1] in a SortedList to maintain sortedness
        sl = SortedList()
        for i in range(n-1):
            sl.add((nums[i] + nums[i+1], i))
        #print(list(sl))
        
        # Count unsorted pairs
        unsorted_pairs = 0
        for i in range(1, n):
            if nums[i] < nums[i-1]:
                unsorted_pairs += 1
        
        # Simulate the process
        moves = 0
        deleted = defaultdict(bool)
        while unsorted_pairs > 0:
            moves += 1
            (S, i) = sl[0]
            # ...
            
            sl.remove((S,i))
        return moves 
            

sol = Solution()
nums = [5,2,3,1]
nums = [1,3,5,7,2,6,2,1,3,10,11,3,12]
print(sol.minimumPairRemoval(nums))
            

        