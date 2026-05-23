from typing import List
class Solution:
    def check(self, nums: List[int]) -> bool:
        n = len(nums)
        for i in range(n):
            if nums[i] > nums[(i+1) % n]:
                if i == n-1:
                    return True 
                else:
                    for j in range(i+1, n):
                        if nums[j] > nums[(j+1) % n]:
                            return False 
        return True
sol = Solution()
nums = [5,3,8,9,2,3,4]
nums = [1]
print(sol.check(nums))
