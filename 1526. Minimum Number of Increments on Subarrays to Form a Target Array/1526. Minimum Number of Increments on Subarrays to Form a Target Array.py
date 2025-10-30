import math 
class Solution:
    def helper(self, target: list[int], damage: int) -> int:
        if len(target) == 0:
            return 0
        if len(target) == 1:
            return target[0]-damage
        
        curr_min = math.inf
        curr_min_idx = 1e9

        for i in range(len(target)):
            if target[i]-damage < curr_min:
                curr_min = target[i]-damage
                curr_min_idx = i

        return self.helper(target[0:curr_min_idx], curr_min+damage) + self.helper(target[curr_min_idx+1:], curr_min+damage) + curr_min

    def minNumberOperations(self, target: list[int]) -> int:
        ans = target[0]
        for i in range(len(target)-1):
            if target[i+1] > target[i]:
                ans += target[i+1] - target[i]

        return ans 
    
sol = Solution()
ex1 = [3,1,5,4,2]
ex2 = [1,2,3,2,1]
ex3 = [3,1,1,2]
print(sol.minNumberOperations(ex3))
        
        