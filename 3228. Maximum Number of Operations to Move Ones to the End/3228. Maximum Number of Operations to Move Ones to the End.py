class Solution:
    def maxOperations(self, s: str) -> int:
        n = len(s)
        zero_chunks = 0
        i = n-1
        ans = 0
        while i >= 0:
            if s[i] == '0':
                zero_chunks += 1
            while i >= 0 and s[i] == '0':
                i -= 1
            while i >= 0 and s[i] == '1':
                ans += zero_chunks
                i -= 1
        return ans
sol = Solution()
s = "1001101"
print(sol.maxOperations(s))

