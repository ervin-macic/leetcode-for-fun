from typing import List
class Solution:
    def minimumBoxes(self, apple: List[int], capacity: List[int]) -> int:
        capacity = sorted(capacity, reverse=True)
        total_apples = sum(apple)
        ans = 0
        capacity_so_far = 0
        for c in capacity:
            if total_apples <= capacity_so_far:
                return ans
            capacity_so_far += c
            ans += 1
        return ans
sol = Solution()
apple = [1,3,2]
capacity = [4,3,1,5,2]
print(sol.minimumBoxes(apple, capacity))
