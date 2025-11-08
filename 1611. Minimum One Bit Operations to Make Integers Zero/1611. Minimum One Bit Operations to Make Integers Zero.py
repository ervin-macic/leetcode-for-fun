class Solution:
    def minimumOneBitOperations(self, n: int) -> int:
        if n == 0:
            return 0
        k = 0
        pow2 = 1
        while (pow2 * 2) <= n:
            pow2 *= 2
            k += 1

        return 2**(k+1)-1-self.minimumOneBitOperations(pow2^n)
    
sol = Solution()
print(sol.minimumOneBitOperations(8))