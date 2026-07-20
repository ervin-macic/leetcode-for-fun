class Solution:
    def rearrangeString(self, s: str, x: str, y: str) -> str:
        if y < x:
            t = sorted(s)
        else:
            t = sorted(s, reverse=True)
        return "".join(t)
sol = Solution()
s = "aabc"
x = "a"
y = "c"
print(sol.rearrangeString(s, x, y))