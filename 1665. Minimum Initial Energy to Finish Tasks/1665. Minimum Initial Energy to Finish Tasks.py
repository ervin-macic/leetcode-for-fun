from typing import List 
from bisect import bisect_left
class Solution:
    def minimumEffort(self, tasks: List[List[int]]) -> int:
        tasks.sort(key=lambda arr: (arr[0]-arr[1]))
        def is_enough(energy: int) -> bool:
            for cost, min_cost in tasks:
                if energy < min_cost:
                    return False 
                energy -= cost 
            return True
        lo = 0
        hi = 0
        for cost, min_cost in tasks:
            lo += cost 
            hi += min_cost
        idx = bisect_left(range(lo, hi+1), True, key=is_enough)
        return idx + lo
            
sol = Solution()
tasks = [[1,3],[2,4],[10,11],[10,12],[8,9]]
tasks = [[1,2],[2,4],[4,8]]
print(sol.minimumEffort(tasks))