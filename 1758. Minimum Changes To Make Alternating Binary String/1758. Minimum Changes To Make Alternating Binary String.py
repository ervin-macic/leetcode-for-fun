class Solution:
    def minOperations(self, s: str) -> int:
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
        return min(ones_even + zeros_odd, ones_odd + zeros_even)