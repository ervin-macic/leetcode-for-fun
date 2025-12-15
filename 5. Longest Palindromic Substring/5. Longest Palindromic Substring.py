class Solution:
    
    def longestPalindrome(self, s: str) -> str:
        if not s:
            return ""

        ans = ""

        def expand(l, r):
            while l >= 0 and r < len(s) and s[l] == s[r]:
                l -= 1
                r += 1
            return s[l+1:r]
        
        for i in range(len(s)):
            ans = max(ans, expand(i, i), expand(i, i+1), key=len)

        return ans


sol = Solution()
s = "anavolimilovana"
print(sol.longestPalindrome(s))
