class Solution:
    def minFlips(self, s: str) -> int:
        zeros_odd, zeros_even, ones_odd, ones_even = 0, 0, 0, 0
        for (i,c) in enumerate(s):
            if c == "0":
                if i % 2 == 0:
                    zeros_even += 1
                else:
                    zeros_odd += 1
            else:
                if i % 2 == 0:
                    ones_even += 1
                else:
                    ones_odd += 1
        n = len(s)
        if n % 2 == 0:
            return min(ones_even + zeros_odd, ones_odd + zeros_even)

        ans = float("inf")
        for i in range(n):
            if s[i] == "0":
                zeros_even, zeros_odd = zeros_odd + 1, zeros_even - 1
                ones_even, ones_odd = ones_odd, ones_even
            else:
                zeros_even, zeros_odd = zeros_odd, zeros_even
                ones_even, ones_odd = ones_odd + 1, ones_even - 1
            curr = min(ones_even + zeros_odd, ones_odd + zeros_even)
            ans = min(ans, curr)
        return ans 
        
        
sol = Solution()
s = "111000"
s = "010"
s = "1110"
print(sol.minFlips(s))