from typing import List
import math
class Solution:
    def sumFourDivisors(self, nums: List[int]) -> int:
        ans = 0
        def has_4_divisors(x) -> int:
            if x < 6 or (math.isqrt(x) * math.isqrt(x) == x):
                return -1
            total = 0
            divisor_sum = 1+x
            for d in range(2, math.isqrt(x) + 1):
                if x % d == 0:
                    total += 2
                    if total > 2:
                        return -1
                    divisor_sum += d + x // d
            if total == 2:
                return divisor_sum
            return -1
        
        for num in nums:
            res = has_4_divisors(num)
            if res != -1: ans += res
        return ans
    
sol = Solution()
nums = [21,4,7]
print(sol.sumFourDivisors(nums))
