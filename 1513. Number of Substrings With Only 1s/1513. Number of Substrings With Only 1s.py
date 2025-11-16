import math
class Solution:
    def numSub(self, s: str) -> int:
        n = len(s)
        prev_zero_idx = -1
        ans = 0
        p = 10**9 + 7
        for i in range(n):
            if s[i] == '0':
                ones = i - prev_zero_idx - 1
                if ones > 0:
                    ans += math.comb(ones+1, 2) 
                    ans %= p
                prev_zero_idx = i
        if s[-1] == '1':
            ones = n - prev_zero_idx - 1
            ans += math.comb(ones+1, 2)
            ans %= p
        return ans 
sol = Solution()
s = "0110111"
s = "111111"
print(sol.numSub(s))
