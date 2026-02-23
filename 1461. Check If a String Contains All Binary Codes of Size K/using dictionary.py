class Solution:
    def hasAllCodes(self, s: str, k: int) -> bool:
        n = len(s)
        exists = {}
        for i in range(n-k+1):
            exists[s[i:i+k]] = True
        return len(exists.keys()) == 1 << k
sol = Solution()
s = "00110110"
k = 2
print(sol.hasAllCodes(s, k))

