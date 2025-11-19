import math
class Solution:
    def findFinalValue(self, nums: list[int], original: int) -> int:
        n = len(nums)
        for i in range(math.ceil(math.log2(max(nums))+1)):
            for j in range(n):
                if nums[j] == original:
                    original *= 2
                    break
        return original

nums = [2,7,9]
original = 4
nums = [5,3,6,1,12]
original = 3
sol = Solution()
print(sol.findFinalValue(nums, original))