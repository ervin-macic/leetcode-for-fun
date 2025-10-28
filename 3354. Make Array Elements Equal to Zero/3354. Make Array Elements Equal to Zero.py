class Solution:
    def countValidSelections(self, nums: list[int]) -> int:
        total_sum = sum(nums)
        cum_sum = 0
        ans = 0
        for num in nums:
            cum_sum += num
            if num == 0:
                if total_sum % 2 == 0 and cum_sum == total_sum // 2:
                    ans += 2
                if total_sum % 2 == 1 and (cum_sum == total_sum // 2 or cum_sum == total_sum // 2 + 1):
                    ans += 1
        return ans 

sol = Solution()
nums = [1,0,2,0,3]
print(sol.countValidSelections(nums))