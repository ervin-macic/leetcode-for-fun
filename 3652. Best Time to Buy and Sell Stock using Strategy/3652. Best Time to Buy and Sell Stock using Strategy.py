from typing import List
class Solution:
    def maxProfit(self, prices: List[int], strategy: List[int], k: int) -> int:
        n = len(prices)
        cum_prices = [0]
        curr = 0
        for p in prices:
            curr += p
            cum_prices.append(curr)
        cum_strat = [0]
        curr = 0
        for (s,p) in zip(strategy, prices):
            curr += s * p
            cum_strat.append(curr)
        total = cum_strat[-1]
        max_profit = 0
        for i in range(n - k + 1):
            prices_sum = cum_prices[i + k] - cum_prices[i + k // 2]
            strat_prices_sum = cum_strat[i + k] - cum_strat[i]
            if max_profit < (prices_sum - strat_prices_sum):
                max_profit = prices_sum - strat_prices_sum
        return total + max_profit

sol = Solution()
prices = [4,2,8]
strategy = [-1,0,1]
k = 2
print(sol.maxProfit(prices, strategy, k))