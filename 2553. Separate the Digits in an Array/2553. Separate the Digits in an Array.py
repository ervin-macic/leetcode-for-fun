from typing import List
class Solution:
    def separateDigits(self, nums: List[int]) -> List[int]:
        ans = []
        def addDigits(num):
            arr = []
            if num == 0:
                arr.append(0)
            while num > 0:
                arr.append(num % 10)
                num //= 10
            for digit in reversed(arr):
                ans.append(digit)

        for num in nums:
            addDigits(num)
        return ans 
sol = Solution()
nums = [13,25,83,77]
print(sol.separateDigits(nums))
            
            