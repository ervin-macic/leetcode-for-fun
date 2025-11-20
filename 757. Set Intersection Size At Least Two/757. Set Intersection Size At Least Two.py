from collections import defaultdict
class Solution:
    def intersectionSizeTwo(self, intervals: list[list[int]]) -> int:
        ans = 0
        intervals.sort() # trivial, 3000*log(3000) ~ 30k
        n = len(intervals)
        leftmost = None
        second_leftmost = None
        for [a,b] in reversed(intervals):
            if leftmost != None:
                # If leftmost and second_leftmost already in interval, continue
                if second_leftmost <= b:
                    continue
                # Only leftmost in interval, update second_leftmost greedily
                elif leftmost <= b:
                    if leftmost != a:
                        leftmost, second_leftmost = a, leftmost
                    else:
                        second_leftmost = leftmost + 1
                    ans += 1
                # No elements chosen so far in interval, pick greedily
                else:
                    leftmost, second_leftmost = a, a+1
                    ans += 2
            else:
                leftmost, second_leftmost = a, a+1
                ans += 2
        return ans


sol = Solution()

intervals = [[1,3],[1,4],[2,5],[3,5]]
intervals = [[1,3],[3,7],[8,9]]
intervals = [[1,2],[2,3],[2,4],[4,5]]
intervals = [[0,2],[0,3],[0,2]]
print(sol.intersectionSizeTwo(intervals))


