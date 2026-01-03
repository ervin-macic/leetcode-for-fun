class Solution:
    def numOfWays(self, n: int) -> int:
        MOD = 10**9+7
        if n == 1:
            return 12
        if n == 2:
            return 54

        g_0 = 6
        g_1 = 30

        for _ in range(3, n + 1):
            g_curr = (5 * g_1 - 2 * g_0) % MOD
            g_0, g_1 = g_1, g_curr

        return (2 * g_1 - g_0) % MOD