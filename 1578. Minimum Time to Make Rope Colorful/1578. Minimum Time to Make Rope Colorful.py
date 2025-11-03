class Solution:
    def minCost(self, colors: str, neededTime: list[int]) -> int:
        # Greedy should work?
        i = 0
        ans = 0
        while i < len(colors):
            current_char = colors[i]
            running_sum = 0
            current_max = -1
            while i < len(colors) and colors[i] == current_char:
                running_sum += neededTime[i]
                if neededTime[i] > current_max:
                    current_max = neededTime[i]
                i += 1
            ans += running_sum - current_max
        return ans
            
sol = Solution()
colors = "abaac" 
neededTime = [1,2,3,4,5]
colors1 = "abc"
neededTime1 = [1,2,3]
colors2 = "aabaa"
neededTime2 = [1,2,3,4,1]
print(sol.minCost(colors2, neededTime2))
                 
