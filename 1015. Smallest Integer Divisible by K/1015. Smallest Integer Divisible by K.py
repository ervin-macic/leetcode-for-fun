class Solution:
    def smallestRepunitDivByK(self, k: int) -> int:
        # Need to find smallest n such that 10^n equiv 1 mod 9n
        if k % 2 == 0 or k % 5 == 0:
            return -1
        if k == 1:
            return 1
        n = 1
        rem = 10
        while rem % (9*k) != 1:
            rem *= 10
            rem %= 9*k 
            n += 1
        return n

sol = Solution()
print(sol.smallestRepunitDivByK(3))
