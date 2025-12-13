from typing import List
class Solution:
    def validateCoupons(self, code: List[str], businessLine: List[str], isActive: List[bool]) -> List[str]:
        n = len(code)
        ans = []
        for i in range(n):
            if len(code[i]) and all(ch.isalnum() or ch == '_' for ch in code[i]) and (businessLine[i] in {"electronics", "grocery", "pharmacy", "restaurant"}) and isActive[i]:
                ans.append((businessLine[i], code[i]))
        ans = [y for (x,y) in sorted(ans)]
        return ans
sol = Solution()
code = ["SAVE20","","PHARMA5","SAVE@20"]
businessLine = ["restaurant","grocery","pharmacy","restaurant"]
isActive = [True,True,True,True]

code = ["GROCERY15","ELECTRONICS_50","DISCOUNT10"]
businessLine = ["grocery","electronics","invalid"]
isActive = [False,True,True]
print(sol.validateCoupons(code, businessLine, isActive))