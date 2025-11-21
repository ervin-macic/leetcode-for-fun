import string
from collections import defaultdict
class Solution:
    def countPalindromicSubsequence(self, s: str) -> int:
        ans = 0
        n = len(s)
        seen_chars = defaultdict(bool)
        for i in range(n):
            if not seen_chars[s[i]]:
                for j in range(n-1, -1, -1):
                    if s[j] == s[i]:
                        break
                if j != i:
                    seen = defaultdict(bool)
                    num_distinct = 0
                    for k in range(j-1, i, -1):
                        if not seen[s[k]]:
                            num_distinct += 1
                            seen[s[k]] = True
                    ans += num_distinct
                seen_chars[s[i]] = True
        return ans 
    
sol = Solution()
s = "aabca"
print(sol.countPalindromicSubsequence(s))
            
                
