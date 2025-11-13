class Solution:
    def canCompleteCircuit(self, gas: list[int], cost: list[int]) -> int:
        n = len(gas)
        total_gas = sum(gas)
        total_cost = sum(cost)
        current_gas = 0
        best_station = 0
        if total_gas >= total_cost:
            for i in range(n):
                # start/continue a chain from position i
                current_gas += gas[i] - cost[i]
                if current_gas < 0:
                    current_gas = 0
                    best_station = i+1
            return best_station
        return -1
        


sol = Solution()
gas = [1,2,3,4,5]
cost = [3,4,5,1,2]
print(sol.canCompleteCircuit(gas, cost))