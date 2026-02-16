from math import log2, floor
class Solution:
    def reverseBits(self, n: int) -> int:
        pow2 = 2 ** 31
        ans = 0
        while pow2 > 0:
            d = n % 2 
            n //= 2
            ans += d * pow2
            pow2 //= 2
        return ans

n = 43261596
sol = Solution()
print(sol.reverseBits(n))