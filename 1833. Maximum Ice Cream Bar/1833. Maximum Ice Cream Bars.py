class Solution:
    def maxIceCream(self, costs: list[int], coins: int) -> int:
        M = max(costs)
        C = [0] * (M+1)
        for c in costs:
            C[c] += 1
        i = 0
        ans = 0
        while i <= M and coins > 0:
            if C[i] > 0:
                if coins >= i * C[i]:
                    coins -= i * C[i]
                    ans += C[i]
                else:
                    ans += coins // i
                    break 
            i += 1
        return ans
costs = [1,6,3,1,2,5]
coins = 20
sol = Solution()
print(sol.maxIceCream(costs,coins))
    

        