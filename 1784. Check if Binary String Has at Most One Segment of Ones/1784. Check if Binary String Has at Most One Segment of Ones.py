class Solution:
    def checkOnesSegment(self, s: str) -> bool:
        n = len(s)
        i = 0
        while i < n and s[i] == "1":
            i += 1
        while i < n and s[i] == "0":
            i += 1
        return (i == n)

sol = Solution()
s = "111000"
print(sol.checkOnesSegment(s))
