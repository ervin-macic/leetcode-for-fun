class Solution:
    def countBinarySubstrings(self, s: str) -> int:
        start_bit = s[0]
        run = prev_run = 0
        idx = 0
        ans = 0
        while idx < len(s):
            # print(prev_run, run)
            start_bit = s[idx]
            run = 0
            while idx < len(s) and s[idx] == start_bit:
                idx += 1
                run += 1
            ans += min(prev_run, run)
            prev_run = run
        return ans 
sol = Solution()
s = "00110011"
print(sol.countBinarySubstrings(s))