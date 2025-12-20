from typing import List
class Solution:
    def minDeletionSize(self, strs: List[str]) -> int:
        ans = 0
        m = len(strs[0])
        n = len(strs)
        for c in range(m):
            for i in range(1, n):
                if strs[i][c] < strs[i-1][c]:
                    ans += 1
                    break 
        return ans
            
sol = Solution()
strs = ["zyx","wvu","tsr"]
print(sol.minDeletionSize(strs))