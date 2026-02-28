from math import log2, floor
class Solution:
    def concatenatedBinary(self, n: int) -> int:
        MOD = 10**9 + 7
        total = 0
        for i in range(1, n + 1):
            total = ((total << i.bit_length()) + i) % MOD
        return total

