class Solution:
    def majorityElement(self, nums: list[int]) -> int:
        candidate = nums[0]
        cnt = 0
        for num in nums:
            if num != candidate:
                if cnt == 0:
                    candidate = num 
                    cnt = 1
                else:
                    cnt -= 1
            else:
                cnt += 1
        return candidate 
sol = Solution()
nums = [2,2,1,1,1,2,2]
print(sol.majorityElement(nums))