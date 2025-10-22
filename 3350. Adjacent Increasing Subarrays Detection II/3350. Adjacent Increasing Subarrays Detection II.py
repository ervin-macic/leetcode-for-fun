
class Solution:
    def maxIncreasingSubarrays(self, nums: list[int]) -> int:
        prev_run = 0
        run = 1
        best_adjacent = 1
        max_run = 1
        for i in range(1,len(nums)):
            if nums[i] > nums[i-1]:
                # Increment current run
                run += 1
            else:
                # Reset for next pair
                prev_run = run
                run = 1
            # Update max_run and best_adjacent
            if max_run < run:
                    max_run = run
            if best_adjacent < min(prev_run, run):
                    best_adjacent = min(prev_run, run)
        # Either chop the longest in half or take two adjacent runs
        return max(max_run // 2, best_adjacent)

sol = Solution()
nums = [2,5,7,8,9,2,3,4,3,1]
k = 3
nums2 = [1,2,3,4,4,4,4,5,6,7]
k2 = 5
nums3 = [-15,19]
k3 = 1
nums4 = [5,8,-2,-1]
k4 = 2
print(sol.maxIncreasingSubarrays(nums))
        