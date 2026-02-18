class Solution:
    def hasAlternatingBits(self, n: int) -> bool:
        result = True
        prev_bit = -1
        while n > 0:
           next_bit = n & 1
           if next_bit == prev_bit:
              result = False 
              break 
           prev_bit = next_bit
           n >>= 1
        return result

sol = Solution()
print(sol.hasAlternatingBits(15))