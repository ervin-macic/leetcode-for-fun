import heapq
from typing import List 

class Solution:
    def minStoneSum(self, piles: List[int], k: int) -> int:
        total = sum(piles)
        heapq.heapify_max(piles)
        for _ in range(k):
            maxPile = heapq.heappop_max(piles)
            total -= maxPile // 2
            maxPile -= maxPile // 2
            heapq.heappush_max(piles, maxPile)
        return total

sol = Solution()
piles = [4,3,6,7]
k = 3
print(sol.minStoneSum(piles, k))
