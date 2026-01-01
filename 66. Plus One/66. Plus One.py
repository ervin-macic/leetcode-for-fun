from typing import List
class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        num_digits = len(digits)
        for i in range(num_digits - 1, -1, -1):
            if digits[i] != 9:
                digits[i] += 1
                return digits
            else:
                digits[i] = 0
        ans = [1] + [0 for _ in range(num_digits)]
        return ans
    
sol = Solution()
digits = [4,3,2,1]
digits = [1,2,3]
digits = [8, 9, 9, 9]
digits = [9,9,9]
print(sol.plusOne(digits))