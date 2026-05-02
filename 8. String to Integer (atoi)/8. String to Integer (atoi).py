class Solution:
    def myAtoi(self, s: str) -> int:
        i = 0
        n = len(s)

        while i < n and s[i] == ' ':
            i += 1
        if i == n:
            return 0

        sign = 1
        if s[i] == '-':
            sign = -1
            i += 1
        elif s[i] == '+':
            i += 1

        x = 0
        while i < n and s[i].isdigit():
            x = x * 10 + int(s[i])
            i += 1

        x *= sign

        INT_MIN = -2**31
        INT_MAX = 2**31 - 1

        if x < INT_MIN:
            return INT_MIN
        if x > INT_MAX:
            return INT_MAX

        return x
sol = Solution()
s = "  -12asdw 34"
print(sol.myAtoi(s))