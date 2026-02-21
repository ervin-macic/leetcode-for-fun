class Solution:
    def makeLargestSpecial(self, s: str) -> str:
        def getCatalans(s: str) -> list[str]:
            catalans = []
            ones = 0
            zeros = 0
            start = 0
            for (i, c) in enumerate(s):
                if c == '1':
                    ones += 1
                else:
                    zeros += 1
                if ones == zeros:
                    catalans.append(s[start:(i+1)])
                    start = i+1
            return catalans
        
        catalans = getCatalans(s)
        if len(catalans) == 1:
            return s[0] + self.makeLargestSpecial(s[1:-1]) + s[-1]
        catalans = [self.makeLargestSpecial(C) for C in catalans]
        catalans.sort(reverse=True)
        return "".join(catalans)

sol = Solution()
s = "11011000"
print(sol.makeLargestSpecial(s))