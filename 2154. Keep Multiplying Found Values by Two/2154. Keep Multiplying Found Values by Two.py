class Solution:
    def findFinalValue(self, nums: list[int], original: int) -> int:
        nums.sort()
        n = len(nums)
        target = original
        for i in range(n):
            if nums[i] > target:
                break
            if nums[i] == target:
                target *= 2
        return target

nums = [5,3,6,1,12]
original = 3
nums = [2,7,9]
original = 4
sol = Solution()
print(sol.findFinalValue(nums, original))