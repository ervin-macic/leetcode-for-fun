class Solution:
    def maxDistinctElements(self, nums: list[int], k: int) -> int:
        nums.sort()
        ans = 0
        prev = -1e20
        if k < 0:
            k *= -1
        for num in nums:
            curr = min(max(num - k, prev+1), num+k)
            if curr >= prev+1:
                ans += 1
                prev = curr
        return ans
    
sol = Solution()
nums = [1,2,2,3,3,4]
k = 2
nums2 = [4,4,4,4]
k2 = 1
print(sol.maxDistinctElements(nums, k))

        