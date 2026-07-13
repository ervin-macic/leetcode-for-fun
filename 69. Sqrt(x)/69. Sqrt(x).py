from bisect import bisect_left
class Solution:
    def mySqrt(self, x: int) -> int:
        if x == 0 or x == 1: return x
        return bisect_left(range(1, x), True, key=lambda y: y * y > x)
sol = Solution()
x = 1
print(sol.mySqrt(x))