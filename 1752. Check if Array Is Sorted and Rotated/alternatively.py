class Solution:
    def check(self, nums: list[int]) -> bool:
        n = len(nums)
        cnt = 0
        for i in range(n):
            if nums[i] > nums[i-1]:
                cnt += 1
            if cnt == 2:
                return False 
        return True