class Solution:
    def firstMissingPositive(self, nums: List[int]) -> int:
        n = len(nums)
        i = 0
        while i < n:
            curr = nums[i]
            nums[i] = 0
            while 1 <= curr <= n:
                target = curr - 1
                if nums[target] == curr:
                    break
                curr, nums[target] = nums[target], curr
            i += 1
        for i in range(n):
            if nums[i] != i + 1:
                return i + 1
        return n + 1

sol = Solution()
nums = [3,4,-1,-2,1,5,16,0,2,0]
nums = [3,4,-1, 1]
print(sol.firstMissingPositive(nums))