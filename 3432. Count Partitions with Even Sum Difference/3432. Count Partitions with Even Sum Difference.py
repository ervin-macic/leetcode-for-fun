class Solution:
    def countPartitions(self, nums: List[int]) -> int:
        n = len(nums)
        sum = 0
        for num in nums:
            sum += num % 2
        sum %= 2
        if sum == 0:
            return n-1
        return 0