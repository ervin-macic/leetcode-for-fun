
class Solution:
    def findSmallestInteger(self, nums: list[int], value: int) -> int:
        mex = 0
        rems = [0] * value
        for num in nums:
            rems[num % value] += 1

        j = 0
        while rems[j % value] > 0:
            rems[j % value] -= 1
            j += 1
        return j


nums = [1,-10,7,13,6,8]
value = 5
nums2 = [1,-10,7,13,6,8] 
value2 = 7
nums3 = [3,0,3,2,4,2,1,1,0,4] # 0,0,1,1,2,2,3,3,4,4
value3 = 5
sol = Solution()
print(sol.findSmallestInteger(nums3, value3))
        