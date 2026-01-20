class Solution_brute:
    def minBitwiseArray(self, nums: List[int]) -> List[int]:
        ans = []
        for num in nums:
            if num == 2:
                ans.append(-1)
            else:
                for x in range(num):
                    if x | (x+1) == num:
                        ans.append(x)
                        break
        return ans
    
class Solution:
    def minBitwiseArray(self, nums: List[int]) -> List[int]:
        for i in range(len(nums)):
            if nums[i] == 2:
                nums[i] = -1
            else:
                pow2 = 1
                x = None
                while (nums[i] & pow2) != 0:
                    x = nums[i] - pow2
                    pow2 = pow2 << 1
                nums[i] = x
        return nums