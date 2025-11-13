import math
class Solution:
    def minOperations(self, nums: list[int]) -> int:
        n = len(nums)
        ones = nums.count(1)
        if ones:
            return n - ones
        
        for level in range(1,n):
            for i in range(n-level):
                d = math.gcd(nums[i], nums[i+1])
                # Update nums for next iteration
                nums[i] = d 
                if d == 1:
                    return level + n - 1
        return -1
        



sol = Solution()
nums = [2,6,3,4]
nums = [6,15,10]
nums = [2,10,6,14]
sol.minOperations(nums)