from typing import List
class Solution:
    def minElement(self, nums: List[int]) -> int:
        ans = 10001
        for num in nums:
            digit_sum = 0
            while num > 0:
                digit_sum += num % 10
                num //= 10
            ans = min(ans, digit_sum)
        return ans