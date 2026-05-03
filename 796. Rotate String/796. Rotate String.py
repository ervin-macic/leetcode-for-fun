class Solution:
    def rotateString(self, s: str, goal: str) -> bool:
        n = len(s)
        if n != len(goal):
            return False
        for start in range(n):
            if s[start] != goal[0]:
                continue
            i = 0
            while i < n and s[(start + i) % n] == goal[i]:
                i += 1
            if i == n:
                return True 
        return False 
sol = Solution()
s = "abcde"
goal = "cdeab"
print(sol.rotateString(s, goal))