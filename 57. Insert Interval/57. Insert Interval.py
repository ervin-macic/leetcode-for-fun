from bisect import bisect_left
from collections import deque
class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        a, b = newInterval
        n = len(intervals)
        intervals = deque(intervals)
        if a > intervals[-1][1]:
            intervals.append(newInterval)
            return intervals 
        if b < intervals[0][0]:
            intervals.appendleft(newInterval)
        
        i = bisect_left(intervals, False, key=lambda x: x[1] >= a)
        j = bisect_left(intervals, False, key=lambda x: x[1] >= b)
        intervals = list(intervals)
        
        return None
sol = Solution()
intervals = [[1,3], [6,9]]
newInterval = [2,5]
print(sol.insert(intervals, newInterval))