class Solution:
    def countOperations(self, num1: int, num2: int) -> int:
        ans = 0
        while num1 != 0 and num2 != 0:
            smaller = min(num1, num2)
            larger = max(num1, num2)
            num1 = larger - smaller 
            num2 = smaller
            ans += 1
        return ans
    
sol = Solution()
print(sol.countOperations(10,10))