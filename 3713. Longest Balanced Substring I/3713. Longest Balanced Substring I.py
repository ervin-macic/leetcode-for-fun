from collections import defaultdict
from sortedcontainers import SortedList
class Solution:
    def longestBalanced(self, s: str) -> int:
        n = len(s)
        max_len = 1
        for i in range(n):
            hash = defaultdict(int)
            for j in range(i,n):
                hash[s[j]] += 1
                if len(set(hash.values())) == 1:
                    max_len = max(max_len, j-i+1)
        return max_len

sol = Solution()
s = "zzabccy"
print(sol.longestBalanced(s))