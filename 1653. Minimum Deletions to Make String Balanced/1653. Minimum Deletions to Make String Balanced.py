class Solution:
    def minimumDeletions(self, s: str) -> int:
        as_right = 0
        for c in s:
            if c == 'a':
                as_right += 1
        bs_left = 0
        n = len(s)
        min_ops = float("inf")
        for i in range(n):
            min_ops = min(min_ops, as_right + bs_left)
            if s[i] == 'a':
                as_right -= 1
            else:
                bs_left += 1
        min_ops = min(min_ops, as_right + bs_left)
        return min_ops
sol = Solution()
s = "aababbab"
print(sol.minimumDeletions(s))