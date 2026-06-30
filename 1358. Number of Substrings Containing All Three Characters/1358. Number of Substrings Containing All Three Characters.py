from collections import defaultdict

class Solution:
    def numberOfSubstrings(self, s: str) -> int:
        n = len(s)
        cnt = defaultdict(int)
        ans = 0
        r = 0
        for l in range(n):
            while r < n and not (cnt['a'] and cnt['b'] and cnt['c']):
                cnt[s[r]] += 1
                r += 1
            if cnt['a'] and cnt['b'] and cnt['c']:
                ans += n - r + 1
            cnt[s[l]] -= 1
        return ans
s = "aaacb"
sol = Solution()
print(sol.numberOfSubstrings(s))