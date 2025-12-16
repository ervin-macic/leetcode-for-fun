from typing import List

class Solution:
    def maxProfit(self, n: int, present: List[int], future: List[int], hierarchy: List[List[int]], budget: int) -> int:
        graph = [[] for _ in range(n)]
        for p, c in hierarchy:
            graph[p - 1].append(c - 1)

        def dfs(node: int):
            full_cost = present[node]
            discounted_cost = present[node] // 2

            dp_parent_not_purchased = [0] * (budget + 1)
            dp_parent_purchased = [0] * (budget + 1)

            child_profit_no_discount = [0] * (budget + 1)
            child_profit_with_discount = [0] * (budget + 1)

            total_size = full_cost

            for child in graph[node]:
                child_dp0, child_dp1, child_size = dfs(child)
                total_size += child_size

                for b in range(budget, -1, -1):
                    for cost in range(min(child_size, b) + 1):
                        if b - cost >= 0:
                            child_profit_no_discount[b] = max(
                                child_profit_no_discount[b],
                                child_profit_no_discount[b - cost] + child_dp0[cost],
                            )
                            child_profit_with_discount[b] = max(
                                child_profit_with_discount[b],
                                child_profit_with_discount[b - cost] + child_dp1[cost],
                            )

            for b in range(budget + 1):
                dp_parent_not_purchased[b] = child_profit_no_discount[b]
                dp_parent_purchased[b] = child_profit_no_discount[b]

                if b >= discounted_cost:
                    dp_parent_purchased[b] = max(
                        child_profit_no_discount[b],
                        child_profit_with_discount[b - discounted_cost] + future[node] - discounted_cost
                    )

                if b >= full_cost:
                    dp_parent_not_purchased[b] = max(
                        child_profit_no_discount[b],
                        child_profit_with_discount[b - full_cost] + future[node] - full_cost
                    )

            return dp_parent_not_purchased, dp_parent_purchased, total_size

        dp0, _, _ = dfs(0)
        return dp0[budget]


sol = Solution()
n = 3
present = [4,6,8]
future = [7,9,11]
hierarchy = [[1,2],[1,3]]
budget = 10

# TC 4
n = 3
present = [5,2,3]
future = [8,5,6]
hierarchy = [[1,2],[2,3]]
budget = 7

n = 3
present = [6,4,23]
future = [50, 48, 17]
hierarchy = [[1,3], [1,2]]
budget = 28
print(sol.maxProfit(n, present, future, hierarchy, budget))
