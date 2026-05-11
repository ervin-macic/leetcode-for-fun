from typing import List
class Solution:
    def separateDigits(self, nums: List[int]) -> List[int]:
        ans = []
        for num in nums:
            for d in str(num):
                ans.append(int(d))
        return ans
sol = Solution()
nums = [13,25,83,77]
print(sol.separateDigits(nums))