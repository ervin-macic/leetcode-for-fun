from typing import List
class Solution:
    def maximumHappinessSum(self, happiness: List[int], k: int) -> int:
        happiness = sorted(happiness, reverse=True)
        num_taken = 0
        total = 0
        for h in happiness:
            if num_taken == k:
                break
            total += max(h - num_taken, 0)
            num_taken += 1
        return total

sol = Solution()
happiness = [2,3,4,5]
k = 1
print(sol.maximumHappinessSum(happiness, k))


