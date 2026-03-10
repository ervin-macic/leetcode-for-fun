class Solution:
    def numberOfStableArrays(self, zeros: int, ones: int, limit: int) -> int:
        MOD = 10**9 + 7
        dp = [[[0]*(ones+1) for _ in range(zeros+1)] for _ in range(2)]

        for z in range(min(zeros, limit)+1):
            dp[0][z][0] = 1
        for o in range(min(ones, limit)+1):
            dp[1][0][o] = 1

        for z in range(1, zeros+1):
            for o in range(1, ones+1):
                if z > limit:
                    dp[0][z][o] = dp[0][z-1][o] + dp[1][z-1][o] - dp[1][z-limit-1][o]
                else:
                    dp[0][z][o] = dp[0][z-1][o] + dp[1][z-1][o]
                dp[0][z][o] %= MOD

                if o > limit:
                    dp[1][z][o] = dp[1][z][o-1] + dp[0][z][o-1] - dp[0][z][o-limit-1]
                else:
                    dp[1][z][o] = dp[1][z][o-1] + dp[0][z][o-1]
                dp[1][z][o] %= MOD

        return (dp[0][zeros][ones] + dp[1][zeros][ones]) % MOD