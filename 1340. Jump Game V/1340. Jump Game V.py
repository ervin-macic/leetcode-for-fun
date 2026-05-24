class Solution:
    def maxJumps(self, nums: list[int], d: int) -> int:
        n = len(nums)
        # number of different squares you can visit starting from index i
        DP = [0] * n
        if nums[0] <= nums[1]:
            DP[0] = 1
        if nums[-1] <= nums[-2]:
            DP[-1] = 1
        for i in range(1, n-1):
            if nums[i] <= nums[i-1] and nums[i] <= nums[i+1]:
                DP[i] = 1
        def dp(i):
            j = i-1 
            while j >= max(0, i-d) and nums[j] < nums[i]:
                if DP[j] != 0:
                    DP[i] = max(DP[i], DP[j] + 1)
                else:
                    DP[i] = max(DP[i], dp(j) + 1)
                j -= 1
            j = i+1 
            while j < min(i+d+1, n) and nums[j] < nums[i]:
                if DP[j] != 0:
                    DP[i] = max(DP[i], DP[j] + 1)
                else:
                    DP[i] = max(DP[i], dp(j) + 1)
                j += 1
            return DP[i]
        for i in range(n):
            if DP[i] == 0:
                dp(i)
        return max(DP)
            
sol = Solution()
arr = [6,4,14,6,8,13,9,7,10,6,12]
d = 2
print(sol.maxJumps(arr, d))