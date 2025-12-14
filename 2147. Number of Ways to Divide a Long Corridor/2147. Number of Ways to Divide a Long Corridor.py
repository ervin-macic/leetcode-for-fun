MOD = 10**9+7
MOD = 10**9 + 7

class Solution:
    def numberOfWays(self, corridor: str) -> int:
        cnt_S = 0
        ans = 1
        cnt_P = 0
        counting_plants = False

        for ch in corridor:
            if ch == 'S':
                cnt_S += 1
                if cnt_S % 2 == 1 and cnt_S > 2:
                    ans = (ans * (cnt_P + 1)) % MOD
                    cnt_P = 0

                counting_plants = (cnt_S % 2 == 0)

            elif ch == 'P' and counting_plants:
                cnt_P += 1

        if cnt_S < 2 or cnt_S % 2 != 0:
            return 0

        return ans

sol = Solution()
corridor = "SSPPSPS"
print(sol.numberOfWays(corridor))