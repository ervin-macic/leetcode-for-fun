from collections import Counter
class Solution:
    def longestPalindrome(self, s: str) -> int:
        cnt = Counter(s)
        ans = 0
        hasOdd = False 
        for k,v in cnt.items():
            if v % 2 == 0:
                ans += v 
            else:
                hasOdd = True 
                ans += (v-1)
        return ans if not hasOdd else ans+1
sol = Solution()
s = "abccccdd"
print(sol.longestPalindrome(s))