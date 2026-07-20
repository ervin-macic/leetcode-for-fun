from collections import Counter
class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        cnt1 = Counter(magazine)
        cnt2 = Counter(ransomNote)
        for k in cnt2.keys():
            if cnt1[k] < cnt2[k]:
                return False 
        return True
sol = Solution()
ransomNote = "aa"
magazine = "ab"
print(sol.canConstruct(ransomNote, magazine))