from collections import defaultdict
class Solution:
    def minCost(self, source: str, target: str, rules: list[list[str]], costs: list[int]) -> int:
        n = len(source)
        dp = [float("inf")] * n
        i = 0
        patternCost = defaultdict(int)
        for pattern, _ in rules:
            patternCost[pattern] = pattern.count("*")
        
        def matches(word, pattern) -> (bool, int):
            for c, d in zip(word, pattern):
                if c != d and d != '*':
                    return False
            return True
                
        def getPatterns(i) -> list[list[str]]:
            possible_patterns = []
            for pattern, replacement in rules:
                if matches(source[i:], pattern):
                    possible_patterns.append((pattern, replacement))
        
        # would be nice to have a mapping like: (index in source) -> (applicable patterns at that index)
        # feels complex to get this, like O(n) for each index thus 200 * 5000 * 20 for matching so doable in reasonable time
        # IMPORTANT: Once a character position has been used in a rule application, it cannot be used in any later rule application.
        # either a pattern starting with source[i] needed or something earlier is good like abcd and aecd and got abc -> aec
        # roughly: dp[i] = min(dp[i], dp[i+j] + {cost to get source[..(i+j)) == target[..(i+j))}) and run
        # this over all j's that make sense
        # still need to check patterns like source = abc, target = abd only rule abc -> abd for example.

        for i in range(n):
            patterns = getPatterns(i)
            for p in patterns:
                # try DP-style
                dp[i]
        return dp[0]