class Solution:
    def numberOfSubstrings(self, s: str) -> int:
        n = len(s)
        cumsum_zeros = [0]
        cumsum_ones = [0]
        for i in range(n):
            if s[i] == '0':
                cumsum_zeros.append(cumsum_zeros[-1] + 1)
                cumsum_ones.append(cumsum_ones[-1])
            else:
                cumsum_ones.append(cumsum_ones[-1] + 1)
                cumsum_zeros.append(cumsum_zeros[-1])
        ans = 0
        for i in range(n):
            for j in range(i, n):
                # Check i,j inclusive substring
                ones = cumsum_ones[j+1] - cumsum_ones[i]
                zeros = cumsum_zeros[j+1] - cumsum_zeros[i]
                if ones >= zeros * zeros:
                    ans += 1
        return ans
sol = Solution()
s = "101101"
print(sol.numberOfSubstrings(s))

