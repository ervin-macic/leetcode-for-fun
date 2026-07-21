class Solution:
    def maxActiveSectionsAfterTrade(self, s: str) -> int:
        ones = s.count("1")
        s = "1" + s + "1"
        zeroRuns = [len(run) for run in s.split("1") if run > 0]
        if len(zeroRuns) < 2:
            return ones
        return ones + max(zeroRuns[i] + zeroRuns[i+1] for i in range(len(s) - 1))
sol = Solution()
s = "1000100" # 0 -> 1,3,5, 1 -> 0, 2, 4,
print(sol.maxActiveSectionsAfterTrade(s))
            
            