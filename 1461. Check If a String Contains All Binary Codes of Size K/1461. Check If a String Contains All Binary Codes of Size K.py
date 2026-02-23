class Solution:
    def hasAllCodes(self, s: str, k: int) -> bool:
        n = len(s)
        pow2 = 2 ** (k-1)
        exists = [False] * (2*pow2)
        for i in range(n-k+1):
            p2 = pow2 
            current = 0
            for j in range(k):
                bit = ord(s[i+j]) - ord('0')
                current += bit * p2
                p2 //= 2
            exists[current] = True 
        return all(exists) 
sol = Solution()
s = "00110110"
k = 2
print(sol.hasAllCodes(s, k))

