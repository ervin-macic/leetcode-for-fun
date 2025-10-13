class Solution(object):
    def maxProfit(self, K, prices):
        """
        :type k: int
        :type prices: List[int]
        :rtype: int
        """
        # dp[i][k][0/1] represents the largest profit we can make after i days using at most k transactions with/without stock at the end of ith day
        n = len(prices)
        dp = [[[0 for _ in range(2)] for _ in range(K+1)] for _ in range(n)]
        dp[-1][0][0] = 0
        for k in range(K+1):
            dp[-1][k][1] = -10**1000 # impossible situation
            dp[-1][k][0] = 0         # 
        for i in range(n):
            dp[i][0][0] = 0 # with no remaining transactions you can profit 0
        for i in range(1, n):
            for k in range(1, K+1):
                dp[i][k][0] = max(dp[i-1][k][1] + prices[i], dp[i-1][k][0])
                dp[i][k][1] = max(dp[i-1][k-1][0] - prices[i], dp[i-1][k][1])
        return dp[n-1][K][0]

        
def main():
    sol = Solution()
    print(sol.maxProfit(2, [3,2,6,5,0,3]))
main()