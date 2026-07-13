from bisect import bisect_left
import time
class Solution:
    def mySqrt(self, x: float) -> float:
        if x < 0:
            return None
        eps = 1e-5
        curr = x / 2
        while abs(curr * curr - x) > eps:
            curr = curr / 2 + x / (2 * curr)
        return curr

sol = Solution()
x = 20
print(sol.mySqrt(x))