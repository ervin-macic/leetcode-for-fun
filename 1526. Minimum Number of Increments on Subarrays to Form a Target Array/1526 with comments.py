import math 
class Solution:
    def helper(self, target: list[int], damage: int) -> int:
        print("Entering new chunk: ")
        for num in target:
            print(num)
        if len(target) == 0:
            print("This is just length 0")
            return 0
        if len(target) == 1:
            print("This is just length 1")
            return target[0]-damage
        curr_min = math.inf
        curr_min_idx = 1e9
        for i in range(len(target)):
            if target[i]-damage < curr_min:
                curr_min = target[i]-damage
                curr_min_idx = i
        print("Here i am in helper")
        print(f"Curr min idx: {curr_min_idx}")
        return self.helper(target[0:curr_min_idx], curr_min+damage) + self.helper(target[curr_min_idx+1:], curr_min+damage) + curr_min

    def minNumberOperations(self, target: list[int]) -> int:
        print(len(target))
        curr_min = math.inf
        curr_min_idx = 1e9
        for i in range(len(target)):
            if target[i] < curr_min:
                curr_min = target[i]
                curr_min_idx = i
        print(f"Min found: {curr_min} at index {curr_min_idx}")
        print(f"Will run first range to {curr_min_idx} and second from {curr_min_idx+1}")
        ans = self.helper(target[:curr_min_idx], curr_min) + self.helper(target[curr_min_idx+1:], curr_min) + curr_min
        return ans
    
sol = Solution()
ex1 = [3,1,5,4,2]
ex2 = [1,2,3,2,1]
ex3 = [3,1,1,2]
print(sol.minNumberOperations(ex3))
        
        