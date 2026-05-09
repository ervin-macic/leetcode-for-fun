class Solution:
    def maxValue(self, nums: List[int]) -> List[int]:
        n = len(nums)
        ans = [0 for _ in range(n)]
        prev_max = [0 for _ in range(n)]
        best = 0
        for i, num in enumerate(nums):
            if num > nums[best]:
                best = i
            prev_max[i] = best
        def f(r, right_min, right_max):
            pivot_index = prev_max[r]
            p_max = nums[pivot_index]
            curr_max = p_max if p_max <= right_min else right_max
            next_right_min = min(right_min, p_max)
            for i in range(pivot_index, r+1):
                ans[i] = curr_max
                next_right_min = min(next_right_min, nums[i])
            if pivot_index == 0:
                return
            f(pivot_index-1, next_right_min, curr_max)
        f(n-1, 10**10, 0)
        return ans
    
sol = Solution()
nums = [2,3,1]
nums = [11,18,11]
print(sol.maxValue(nums))