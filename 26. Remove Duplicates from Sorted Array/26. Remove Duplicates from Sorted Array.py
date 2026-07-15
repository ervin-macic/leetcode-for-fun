class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        if not nums:
            return 0
        k = 1
        n = len(nums)
        for i in range(1, n):
            if nums[i] != nums[k - 1]:
                nums[k] = nums[i]
                k += 1
        return k

sol = Solution()
nums = [0,0,1,1,1,2,2,3,3,4]
''
[0,0,1,1,1,2,2,3,3,4]
[0,1,2,2,3,3,4,4,4,4]
''
print(sol.removeDuplicates(nums))