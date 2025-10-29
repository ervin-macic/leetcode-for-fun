import math
class Solution:
    def smallestNumber(self, n: int) -> int:
        k = math.floor(math.log2(n)) + 1
        return 2**k - 1

sol = Solution()
print(sol.smallestNumber(339))