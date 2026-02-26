class Solution:
    def numSteps(self, s: str) -> int:
        ans = 0
        s = list(s)
        while len(s) > 1:
            if s[-1] == "0":
                s.pop()
                ans += 1
            else:
                idx = len(s)-1
                while idx >= 0 and s[idx] == "1":
                    s[idx] = "0"
                    idx -= 1
                if idx < 0:
                    s = ["1"] + s 
                else:
                    s[idx] = "1"
                ans += 1
        return ans 

sol = Solution()
s = "1101"
print(sol.numSteps(s))