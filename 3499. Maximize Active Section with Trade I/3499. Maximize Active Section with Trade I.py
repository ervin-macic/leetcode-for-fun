class Solution:
    def maxActiveSectionsAfterTrade(self, s: str) -> int:
        i = 0
        n = len(s)
        blocks = []
        startWith = s[0]
        maxZeros = 0
        ones = 0
        while i < n:
            curr = s[i]
            sz = 0
            while i < n and s[i] == curr:
                i += 1
                sz += 1
                if curr == "0":
                    maxZeros = max(maxZeros, sz)
                else:
                    ones += 1
            blocks.append(sz)
        m = len(blocks)
        ans = ones
        for i, b in enumerate(blocks):
            if i % 2 != int(startWith) and i != 0 and i != m-1:
                zeros = blocks[i-1] + b + blocks[i+1]
                ans = max(ans, ones + (zeros - b))
        return ans

sol = Solution()
s = "1000100" # 0 -> 1,3,5, 1 -> 0, 2, 4,
print(sol.maxActiveSectionsAfterTrade(s))
            
            