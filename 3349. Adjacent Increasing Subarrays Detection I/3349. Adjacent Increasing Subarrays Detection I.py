
class Solution:
    def hasIncreasingSubarrays(self, nums: list[int], k: int) -> bool:
        for i in range(0,len(nums)-2*k+1):

            left_increasing, right_increasing = True, True

            for j in range(1,k):
                if nums[i+j-1] >= nums[i+j]:
                    left_increasing = False

            if left_increasing:
                for j in range(1,k):
                    if nums[i+k+j-1] >= nums[i+k+j]:
                        right_increasing = False
            
            if left_increasing and right_increasing:
                return True 
            
        return False 


sol = Solution()
nums = [2,5,7,8,9,2,3,4,3,1]
k = 3
nums2 = [1,2,3,4,4,4,4,5,6,7]
k2 = 5
nums3 = [-15,19]
k3 = 1
print(sol.hasIncreasingSubarrays(nums, k))
        