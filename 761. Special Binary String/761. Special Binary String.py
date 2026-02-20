class Solution:
    def makeLargestSpecial(self, s: str) -> str:
        if s == "": return ""
        
        def getCatalans(s: str) -> list[str]:
            if s == "": return []
            ones = 1
            zeros = 0
            idx = 1
            while idx < len(s) and (ones - zeros) > 0:
                ones += (s[idx] == '1')
                zeros += (s[idx] == '0')
                idx += 1
            return [s[:idx]] + getCatalans(s[idx:])
        
        catalans = getCatalans(s)
        if len(catalans) == 1:
            return s[0] + self.makeLargestSpecial(s[1:-1]) + s[-1]
        return "".join(sorted([self.makeLargestSpecial(C) for C in catalans], reverse=True))

sol = Solution()
s = "11011000"
print(sol.makeLargestSpecial(s))