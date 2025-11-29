class Solution:
    def minOperations(self, nums: List[int], k: int) -> int:
        return sum(nums) % k


nums = [3,9,7]
k = 5

