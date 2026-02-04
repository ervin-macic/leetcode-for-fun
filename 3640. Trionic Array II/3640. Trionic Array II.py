from typing import List
class Solution:
    def maxSumTrionic(self, nums: List[int]) -> int:
        n = len(nums)
        ans = -float("inf")
        idx = 1
        
        # Get decreasing segments
        decreasing = []
        while True:
            l = idx-1
            s = 0
            while idx < n and nums[idx] < nums[idx-1]:
                s += nums[idx-1]
                idx += 1
            s += nums[idx-1]
            r = idx-1
            if r - l >= 1:
                decreasing.append((l,r,s))
            while idx < n and nums[idx] >= nums[idx-1]:
                idx += 1
            if idx == n:
                break 
        
        # Process each decreasing segment
        # Go left find largest-sum decreasing
        # Go right find largest-sum increasing
        for (l,r,s) in decreasing:

            # Left
            i = l
            max_left_sum = -float("inf")
            left_sum = 0
            while i > 0 and nums[i] > nums[i-1]:
                left_sum += nums[i-1]
                max_left_sum = max(max_left_sum, left_sum)
                i -= 1

            # Right 
            j = r
            max_right_sum = -float("inf")
            right_sum = 0
            while j < n-1 and nums[j] < nums[j+1]:
                right_sum += nums[j+1]
                j += 1
                max_right_sum = max(max_right_sum, right_sum)
            
            # Check whether have valid trionic array and update ans
            if (j-r) >= 1 and (l-i) >= 1:
                total = max_left_sum + s + max_right_sum
                ans = max(ans, total)
        return ans 
        
sol = Solution()
nums = [0,-2,-1,-3,0,2,-1]
nums = [2,993,-791,-635,-569]
nums = [395,731,-892,-619,-238,634]
print(sol.maxSumTrionic(nums))