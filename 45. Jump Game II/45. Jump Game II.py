class Solution:
    def jump(self, nums: List[int]) -> int:
        n = len(nums)
        if n == 1: return 0
        i = 0
        ans = 0
        while True:
            idx = i
            ans += 1
            for j in range(i+1, min(n, i+nums[i]+1)):
                if j == n-1:
                    return ans
                if idx + nums[idx] < j + nums[j]:
                    idx = j 
            i = idx
sol = Solution()
nums = [2,3,1,1,4]
print(sol.jump(nums))
            

