from math import gcd
class Solution:
    def gcdSum(self, nums: list[int]) -> int:
        n = len(nums)
        prefixGCD = [0] * n
        currMax = -float("inf")
        for i in range(n):
            currMax = max(currMax, nums[i])
            prefixGCD[i] = gcd(nums[i], currMax)
        prefixGCD.sort()
        l = 0
        r = n-1
        total = 0
        while l < r:
            total += gcd(prefixGCD[l], prefixGCD[r])
            l += 1
            r -= 1
        return total 
sol = Solution()
nums = [3,6,2,8]
print(sol.gcdSum(nums))

