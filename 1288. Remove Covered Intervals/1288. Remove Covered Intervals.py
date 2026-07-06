from typing import List 
class Solution:
    def removeCoveredIntervals(self, intervals: List[List[int]]) -> int:
        intervals.sort(key=lambda x: (x[0], -x[1]))
        left, right = intervals[0]
        n = len(intervals)
        ans = n
        i = 1
        while i < n:
            next_left, next_right = intervals[i]
            if next_right <= right:
                ans -= 1
            else:
                left = next_left 
                right = next_right
            i += 1
        return ans 
intervals = [[1,4],[3,6],[2,8]]
sol = Solution()
print(sol.removeCoveredIntervals(intervals))