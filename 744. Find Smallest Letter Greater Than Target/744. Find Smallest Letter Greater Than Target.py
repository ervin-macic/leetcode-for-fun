from typing import List
class Solution:
    def nextGreatestLetter(self, letters: List[str], target: str) -> str:
        ans = None
        for c in letters:
            if c > target:
                if ans:
                    ans = min(ans, c)
                else:
                    ans = c
        if ans:
            return ans
        return letters[0]
sol = Solution()
letters = ["c","f","j"]
target = "c"
print(sol.nextGreatestLetter(letters, target))