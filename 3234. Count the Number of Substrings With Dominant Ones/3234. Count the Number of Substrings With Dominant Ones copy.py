class Solution:
    def numberOfSubstrings(self, s: str) -> int:
        n = len(s)
        next_zero = [n] * n
        for i in range(n-2, -1, -1):
            if s[i+1] == '0':
                next_zero[i] = i+1
            else:
                next_zero[i] = next_zero[i+1]
        ans = 0
        for i in range(n):
            j = i
            zeros = int(s[i] == '0')
            while zeros * zeros <= n:
                ones = next_zero[j] - i - zeros
                ans += min(next_zero[j] - j, ones - zeros*zeros + 1) if ones >= zeros * zeros else 0
                # Update j and zeros seen so far
                j = next_zero[j]
                zeros += 1
                if j == n:
                    break
        return ans
sol = Solution()
s = "101101"
print(sol.numberOfSubstrings(s))

