class Solution:
    def totalMoney(self, n: int) -> int:
        q = n // 7
        r = n - 7*q 
        return (7*q*q+r*r+49*q+r+2*q*r)//2

sol = Solution()
print(sol.totalMoney(20))