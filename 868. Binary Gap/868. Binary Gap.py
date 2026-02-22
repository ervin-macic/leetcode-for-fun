class Solution:
    def binaryGap(self, n: int) -> int:
        ans = 0
        # Remove 0s from right
        while n % 2 == 0:
            n //= 2

        while n > 0 and n % 2 == 1:
            if n == 1:
                break 
            # Rightmost bit is 1 here
            n //= 2
            curr = 1
            while n > 0 and n % 2 == 0:
                curr += 1
                n //= 2
            ans = max(ans, curr)
        return ans
sol = Solution()
n = 6
print(sol.binaryGap(n))