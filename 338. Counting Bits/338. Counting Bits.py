class Solution:
    def countBits(self, n: int) -> List[int]:
        ans = []
        def bitCount(n: int) -> int:
            cnt = 0
            while n > 0:
                n = n & (n-1)
                cnt += 1
            return cnt
        for i in range(n+1):
            ans.append(bitCount(i))
        return ans
