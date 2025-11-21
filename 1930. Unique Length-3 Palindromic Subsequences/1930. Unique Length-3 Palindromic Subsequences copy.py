import string
from collections import defaultdict
class Solution:
    def countPalindromicSubsequence(self, s: str) -> int:
        ans = 0
        n = len(s)
        first = [-1] * 26
        last = [-1] * 26
        for i in range(n):
            code = ord(s[i]) - ord("a")
            if first[code] == -1:
                first[code] = i 
            else:
                last[code] = i
        for i in range(26):
            if first[i] != -1:
                seen = defaultdict(bool)
                distinct = 0
                for j in range(first[i]+1, last[i]):
                    if not seen[s[j]]:
                        distinct += 1
                        seen[s[j]] = True 
                ans += distinct
        return ans 
    
sol = Solution()
s = "aabca"
print(sol.countPalindromicSubsequence(s))
            
                
