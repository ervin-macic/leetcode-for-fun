from collections import Counter

class Solution:
    def findAnagrams(self, s: str, p: str) -> List[int]:
        n, m = len(s), len(p)
        if m > n:
            return []
        pcnt = Counter(p)
        window = Counter(s[:m])
        ans = []
        if window == pcnt:
            ans.append(0)
        for i in range(m, n):
            window[s[i]] += 1
            window[s[i - m]] -= 1
            if window[s[i - m]] == 0:
                del window[s[i - m]]
            if window == pcnt:
                ans.append(i - m + 1)
        return ans
    
sol = Solution()
s = "cbaebabacd"
p = "abc"
s = "abab"
p = "ab"
print(sol.findAnagrams(s, p))
        