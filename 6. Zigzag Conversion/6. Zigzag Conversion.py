class Solution:
    def convert(self, s: str, numRows: int) -> str:
        n = numRows
        m = len(s)
        if m == 1 or n == 1: return s
        ans = []
        row = 0
        while row < n:
            even = True
            d_even, d_odd = 0, 0
            if row % (n-1) == 0:
                d_even = d_odd = 2*(n-1)
            else:
                d_even, d_odd = 2*(n-1-row), 2*row
            i = row
            while i < m:
                ans.append(s[i])
                if even:
                    i += d_even
                    even = False
                else:
                    i += d_odd
                    even = True
            row += 1
        return "".join(ans)
sol = Solution()
s = "PAYPALISHIRING"
numRows = 4
print(sol.convert(s, numRows))

