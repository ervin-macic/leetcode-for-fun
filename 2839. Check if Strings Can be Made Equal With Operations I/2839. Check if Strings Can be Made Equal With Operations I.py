from collections import defaultdict
class Solution:
    def canBeEqual(self, s1: str, s2: str) -> bool:
        seen = defaultdict(bool)
        s1_candidates = [s1, "".join([s1[2], s1[1], s1[0], s1[3]]), "".join([s1[0], s1[3], s1[2], s1[1]])
                      , "".join([s1[2], s1[3], s1[0], s1[1]])]
        s2_candidates = [s2, "".join([s2[2], s2[1], s2[0], s2[3]]), 
                      "".join([s2[0], s2[3], s2[2], s2[1]]), "".join([s2[2], s2[3], s2[0], s2[1]])]
        for c in s1_candidates:
            seen[c] = True 
        
        for c in s2_candidates:
            if seen[c]:
                return True
        return False 
    
sol = Solution()
s1 = "abcd"
s2 = "cdab"
s1 = "abcd"
s2 = "dacb"
s1 = "zzon"
s2 = "zozn"
print(sol.canBeEqual(s1, s2))