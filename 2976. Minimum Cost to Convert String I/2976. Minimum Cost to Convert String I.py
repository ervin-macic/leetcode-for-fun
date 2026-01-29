from typing import List
from typing import List
class Solution:
    def minimumCost(self, source: str, target: str, original: List[str], changed: List[str], cost: List[int]) -> int:
        n = len(source)
        m = len(original)
        dp = [[float("inf") for _ in range(26)] for _ in range(26)]

        for i in range(m):
            o = ord(original[i]) - ord("a")
            c = ord(changed[i]) - ord("a")
            if o == c:
                dp[o][c] = 0
            else:
                dp[o][c] = min(dp[o][c], cost[i])
        
        for k in range(26):
            for i in range(26):
                for j in range(26):
                    dp[i][j] = min(dp[i][j], dp[i][k] + dp[k][j])
        
        total = 0
        possible = True
        for i in range(n):
            s = ord(source[i]) - ord("a")
            t = ord(target[i]) - ord("a")
            if s != t:
                if dp[s][t] == float("inf"):
                    possible = False
                else: 
                    total += dp[s][t]
            if not possible:
                return -1
        return total

sol = Solution()
source = "abcd"
target = "acbe"
original = ["a","b","c","c","e","d"]
changed = ["b","c","b","e","b","e"]
cost = [2,5,5,1,2,20]
print(sol.minimumCost(source, target, original, changed, cost))