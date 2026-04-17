from typing import List
class Solution:
    def minMirrorPairDistance(self, nums: List[int]) -> int:
        def reverse_int(x: int):
            y = 0
            while x:
                y = y * 10 + x % 10
                x //= 10
            return y
        pos = {}
        ans = 10 ** 6
        for i, x in enumerate(nums):
            if x in pos:
                ans = min(ans, i - pos[x])
            pos[reverse_int(x)] = i
        return -1 if ans == 10 ** 6 else ans

nums = [12,21,45,33,54]
sol = Solution()
print(sol.minMirrorPairDistance(nums))