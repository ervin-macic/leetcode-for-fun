from collections import Counter
class Solution:
    def smallestSubsequence(self, s: str) -> str:
        n = len(s)
        freq = Counter(s)
        stack = []
        seen = defaultdict(bool)
        for i in range(n):
            freq[s[i]] -= 1
            if seen[s[i]]:
                continue
            while stack and stack[-1] > s[i] and freq[stack[-1]]:
                seen[stack.pop()] = False 
            stack.append(s[i])
            seen[s[i]] = True 
        return "".join(stack)


        
sol = Solution()
s = "bcadbcacegabef"
print(sol.smallestSubsequence(s))