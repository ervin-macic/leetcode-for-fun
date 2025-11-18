class Solution:
    def isOneBitCharacter(self, bits: list[int]) -> bool:
        n = len(bits)
        if n == 0:
            return True
        if n == 1:
            # 0 1
            return (bits[0] == 0)
        if n == 2:
            # 00 01 10 11
            return (bits[0] != 1)
        i = 0
        while i < n-1:
            if bits[i] == 0:
                i += 1
            else:
                i += 2
        return i == n-1

sol = Solution()
bits = [1,0,0]
print(sol.isOneBitCharacter(bits))
        