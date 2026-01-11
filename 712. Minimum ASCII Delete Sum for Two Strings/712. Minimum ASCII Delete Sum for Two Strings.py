class Solution:
    def minimumDeleteSum(self, s1: str, s2: str) -> int:
        n1, n2 = len(s1), len(s2)
        dp = [[0 for _ in range(n2+1)] for _ in range(n1+1)]
        for i in range(n1 - 1, -1, -1):
            dp[i][n2] = dp[i+1][n2] + ord(s1[i])
        for j in range(n2 - 1, -1, -1):
            dp[n1][j] = dp[n1][j+1] + ord(s2[j])
        for i in range(n1 - 1, -1, -1):
            for j in range(n2 - 1, -1, -1):
                if s1[i] == s2[j]:
                    dp[i][j] = dp[i+1][j+1]
                else: 
                    dp[i][j] = min(dp[i+1][j] + ord(s1[i]), dp[i][j+1] + ord(s2[j]))
        return dp[0][0]

sol = Solution()
s1 = "ccaccjp"
s2 = "fwosarcwge"
print(sol.minimumDeleteSum(s1, s2))