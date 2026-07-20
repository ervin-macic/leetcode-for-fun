from collections import defaultdict
class Solution:
    def minAdjacentSwaps(self, nums: list[int], a: int, b: int) -> int:
        MOD = 10**9 + 7
        n = len(nums)
        ans = 0
        # get < a indices
        smallSeen = 0
        largeSeen = 0
        for i in range(n):
            if nums[i] < a:
                ans += (i-smallSeen)
                smallSeen += 1
                ans -= largeSeen
            elif nums[i] > b:
                largeSeen += 1
        largeSeen = 0
        for i in range(n-1, -1, -1):
            if nums[i] > b:
                ans += (n-1-largeSeen-i)
                largeSeen += 1
        return ans % MOD 
sol = Solution()
nums = [945, 461]
a = 380
b = 868
nums = [1,3,2,4,5,6]
a = 3
b = 4
nums = [3,7,5,9]
a = 4
b = 8
nums = [9,7,5,3]
a = 4
b = 8



print(sol.minAdjacentSwaps(nums, a, b))