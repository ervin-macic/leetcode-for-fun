from typing import List
class Solution:
    def minimumPairRemoval(self, nums: List[int]) -> int:
        moves = 0
        while True:
            n = len(nums)
            min_sum = float('inf')
            min_sum_idx = 0
            is_sorted = True
            for i in range(1, n):
                if nums[i] + nums[i-1] < min_sum:
                    min_sum = nums[i] + nums[i-1]
                    min_sum_idx = i-1
            moves += 1
            nums[min_sum_idx] = min_sum
            for i in range(min_sum_idx + 1, n-1):
                nums[i] = nums[i+1]
            nums.pop()
            for i in range(1, len(nums)):
                if nums[i] < nums[i-1]:
                    is_sorted = False
            if is_sorted:
                return moves
        
nums = [5,2,3,1]
sol = Solution()
print(sol.minimumPairRemoval(nums))



        