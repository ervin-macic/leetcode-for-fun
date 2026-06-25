class Solution:
    def zigZagArrays(self, n: int, l: int, r: int) -> int:
        MOD = 10**9 + 7
        m = r - l + 1

        if n == 1:
            return m

        # dp[len][0][x]: last move was up
        # dp[len][1][x]: last move was down
        up = [0] * m
        down = [0] * m

        # length = 2
        for j in range(m - 2, -1, -1):
            up[j] = up[j + 1] + 1

        for j in range(1, m):
            down[j] = down[j - 1] + 1

        up = [x % MOD for x in up]
        down = [x % MOD for x in down]

        if n == 2:
            return (sum(up) + sum(down)) % MOD

        for _ in range(3, n + 1):
            new_up = [0] * m
            new_down = [0] * m

            for j in range(m - 2, -1, -1):
                new_up[j] = (new_up[j + 1] + down[j + 1]) % MOD

            for j in range(1, m):
                new_down[j] = (new_down[j - 1] + up[j - 1]) % MOD

            up, down = new_up, new_down

        return (sum(up) + sum(down)) % MOD