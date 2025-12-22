from typing import List
from collections import defaultdict
class Solution:
    def minDeletionSize(self, strs: List[str]) -> int:
        ans = 0
        m = len(strs[0])
        n = len(strs)
        fixed = defaultdict(bool)
        for col in range(m):
            conflict = False
            for i in range(n-1):
                if not fixed[i] and strs[i][col] > strs[i+1][col]:
                    conflict = True
                    break
            if conflict:
                ans += 1
                continue
            
            for i in range(n-1):
                if strs[i][col] < strs[i+1][col]:
                    fixed[i] = True
        return ans

            
sol = Solution()
strs = ["xga", "xfb", "yfa", "ygb"]
strs = ["xga", "xfb", "yfa"]

print(sol.minDeletionSize(strs))