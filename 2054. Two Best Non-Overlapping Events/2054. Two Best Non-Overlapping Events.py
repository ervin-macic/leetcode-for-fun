from typing import List
from bisect import bisect_right, bisect_left
class Solution:
    def maxTwoEvents(self, events: List[List[int]]) -> int:
        events = sorted(events)
        max_right = 0
        best_right = []
        for [start, finish, value] in reversed(events):
            if value > max_right:
                max_right = value
                best_right.append((start, value))
        best_right = list(reversed(best_right))
        best = 0
        current = 0
        m = len(best_right)
        for [start, finish, value] in events:
            current = value
            # Find max-valued event with start time > finish time of this event
            idx = bisect_left(best_right, (finish + 1, 0))
            if idx < m:
                (s, v) = best_right[idx]
                current += v
            if current > best:
                best = current
        return best

sol = Solution()

events = [[1,3,2],[4,5,2],[1,5,5],[5,6,10],[4,8,7],[6,8,6]]
events = [[1,3,2],[4,5,2],[1,5,5]]
print(sol.maxTwoEvents(events))