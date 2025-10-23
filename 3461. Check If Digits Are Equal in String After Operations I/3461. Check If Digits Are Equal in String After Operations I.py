import math
class Solution:
    def hasSameDigits(self, s: str) -> bool:
        n = len(s)
        nums = [ord(ch) - 48 for ch in s]
        pascal_vector = [1]
        for i in range(1, n - 1):
            pascal_vector.append(pascal_vector[-1] * (n - i - 1) // i)
        a = sum(x * y for (x,y) in zip(nums[:-1], pascal_vector)) % 10
        b = sum(x * y for (x,y) in zip(nums[1:], pascal_vector)) % 10
        return a == b

sol = Solution()
print(sol.hasSameDigits("34789"))