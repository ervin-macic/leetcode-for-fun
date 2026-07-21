# The isBadVersion API is already defined for you.
def isBadVersion(version: int) -> bool:
    return version > 37
from bisect import bisect_left
class Solution:
    def firstBadVersion(self, n: int) -> int:
        return bisect_left(range(1, n+1), True, key=isBadVersion) + 1

sol = Solution()
print(sol.firstBadVersion(100))