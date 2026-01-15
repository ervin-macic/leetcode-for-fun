from typing import List
class Solution:
    def maximizeSquareHoleArea(self, n: int, m: int, hBars: List[int], vBars: List[int]) -> int:
        hBars.sort()
        vBars.sort()
        curr_consecutive = 1
        h = 1
        for i in range(1, len(hBars)):
            if hBars[i] == hBars[i-1] + 1:
                curr_consecutive += 1
            else:
                curr_consecutive = 1
            h = max(h, curr_consecutive)
        curr_consecutive = 1
        v = 1
        for i in range(1, len(vBars)):
            if vBars[i] == vBars[i-1] + 1:
                curr_consecutive += 1
            else:
                curr_consecutive = 1
            v = max(v, curr_consecutive)

        return (min(h,v) + 1) ** 2
sol = Solution()
n = 2
m = 3
hBars = [2,3]
vBars = [2,4]
print(sol.maximizeSquareHoleArea(n,m,hBars,vBars))
        