import math
class Solution:
    def maxSubarraySum(self, nums: list[int], k: int) -> int:
        n = len(nums)
        ksum = sum(nums[:k])
        k_subarray_sums = [ksum]
        for i in range(1,n-k+1):
            # Get sum of k-length segment
            ksum += nums[i+k-1] - nums[i-1] 
            k_subarray_sums.append(ksum)
        ans = ksum
        m = len(k_subarray_sums)
        for r in range(k):
            if r >= m:
                 break
            # Find max subarray sum in k_subarray_sum on indices that are r mod k
            best_overall = k_subarray_sums[r]
            best_here = k_subarray_sums[r]
            for q in range(1,(m-r-1)//k + 1):
                best_here = max(best_here + k_subarray_sums[k * q + r], k_subarray_sums[k * q + r])
                best_overall = max(best_overall, best_here)
            ans = max(ans, best_overall)
        return ans

def kadane(nums: list[int]) -> int:
        n = len(nums)
        maxsum_overall = 0
        current_maxsum = 0
        for i in range(n):
             current_maxsum = max(current_maxsum+nums[i], 0)
             maxsum_overall = max(maxsum_overall, current_maxsum)
        return maxsum_overall
sol = Solution()
nums = [-5,1,2,-3,4]
k = 2
nums = [-1,-2,-3,-4,-5]
k = 4
print(sol.maxSubarraySum(nums, k))