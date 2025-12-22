from typing import List
class Solution:
    def minDeletionSize(self, strs: List[str]) -> int:
        n = len(strs)
        m = len(strs[0])
        dp = [1] * m
        for i in range(m-1,-1,-1):
            for j in range(i+1,m):
                good_pair = True
                for k in range(n):
                    if strs[k][i] > strs[k][j]:
                        good_pair = False 
                        break
                if good_pair:
                    dp[i] = max(dp[j] + 1, dp[i])
        max_dp = -1
        for k in range(m):
            if dp[k] > max_dp:
                max_dp = dp[k]
        return m - max_dp                