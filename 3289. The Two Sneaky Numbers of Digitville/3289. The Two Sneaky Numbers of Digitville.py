import math
from collections import defaultdict
class Solution:
    def getSneakyNumbers1(self, nums: list[int]) -> list[int]:
        n = len(nums)
        d = defaultdict(int)
        ans = []
        for i in range(n):
            if d[nums[i]] == 1:
                ans.append(nums[i])
            else:
                d[nums[i]] = 1
        return ans
    def getSneakyNumbers(self, nums: list[int]) -> list[int]:
        n = len(nums)-2
        normal_sum = sum(nums)
        squared_sum = 0
        for num in nums:
            squared_sum += num * num
        x = normal_sum - (n*(n-1))//2
        y = squared_sum - (n*(n-1)*(2*n-1))//6
        a = int(x+math.sqrt(2*y-x*x))//2
        b = int(x-math.sqrt(2*y-x*x))//2
        return [a,b]


sol = Solution()
nums = [7,1,5,4,3,4,6,0,9,5,8,2]
print(sol.getSneakyNumbers(nums))