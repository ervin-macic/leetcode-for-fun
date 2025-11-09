class Solution:
    def countOperations(self, num1: int, num2: int) -> int:
        ans = 0
        while num1 != 0 and num2 != 0:
            smaller = min(num1, num2)
            larger = max(num1, num2)
            num1 = smaller 
            quot = (larger // smaller) 
            num2 = larger % smaller
            ans += quot
        return ans


# 2,3 -> 3 
# 3, 17 -> 3, 17 - (17//3) * 3
sol = Solution()
print(sol.countOperations(2,3))