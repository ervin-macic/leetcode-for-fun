class Solution:
    def hasAllCodes(self, s: str, k: int) -> bool:
        n = len(s)
        exists = set()
        total_codes = 1 << k
        for i in range(n-k+1):
            exists.add(s[i:i+k])
        return len(exists) == total_codes