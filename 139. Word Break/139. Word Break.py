from collections import defaultdict
class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        n = len(s)
        dp = {}
        def solve(i) -> bool:
            if i == n:
                return True
            if i in dp:
                return dp[i]
            possible = False
            for w in wordDict:
                if s.startswith(w, i) and solve(i + len(w)):
                    possible = True
                    break
            dp[i] = possible
            return possible
        return solve(0)

sol = Solution()
s = "applepenapple"
wordDict = ["apple","pen"]
s = "catsandog"
wordDict = ["cats","dog","sand","and","cat"]

print(sol.wordBreak(s, wordDict))
            
