class Solution:
    def countBits(self, n: int) -> list[int]:
        ans = [0]
        pow2 = 1
        for m in range(1, n+1):
            if pow2 * 2 == m:
                pow2 = m
            ans.append(ans[m - pow2] + 1)
        return ans
