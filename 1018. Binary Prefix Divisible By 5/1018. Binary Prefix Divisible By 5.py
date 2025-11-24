class Solution:
    def prefixesDivBy5(self, nums: List[int]) -> List[bool]:
        n = len(nums)
        current = 0
        ans = [False] * n
        for i in range(n):
            current = current * 2
            current += nums[i]
            current %= 5
            if current == 0:
                ans[i] = True
        return ans