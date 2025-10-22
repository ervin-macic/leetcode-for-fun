
class Solution:
    def hasIncreasingSubarrays(self, nums: list[int], k: int) -> bool:
        prev_run = 1
        run = 1
        for i in range(1,len(nums)):
            if nums[i] > nums[i-1]:
                run += 1
            else:
                prev_run = run
                run = 1
            if prev_run >= k and run >= k:
                return True
            
        return False 


sol = Solution()
nums = [2,5,7,8,9,2,3,4,3,1]
k = 3
nums2 = [1,2,3,4,4,4,4,5,6,7]
k2 = 5
nums3 = [-15,19]
k3 = 1
nums4 = [5,8,-2,-1]
k4 = 2
print(sol.hasIncreasingSubarrays(nums4, k4))
        