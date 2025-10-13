class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        n = len(prices)
        dp = [[0,0] for _ in range(n+1)]
        dp[-1][0] = 0
        dp[-1][1] = -10000

        for i in range(len(prices)):
            dp[i][0] = max(dp[i-1][1] + prices[i], dp[i-1][0])
            dp[i][1] = max(dp[i-1][0] - prices[i], dp[i-1][1])
        
        return dp[n-1][0]

def main():
    prices = [7,1,5,3,6,4]
    sol = Solution()
    print(sol.maxProfit(prices))
main() 