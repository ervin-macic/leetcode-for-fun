from typing import List
class Solution:
    def twoEditWords(self, queries: List[str], dictionary: List[str]) -> List[str]:
        ans = []
        for q in queries:
            for d in dictionary:
                mismatch = 0
                for i in range(len(q)):
                    if q[i] != d[i]:
                        mismatch += 1
                if mismatch <= 2:
                    ans.append(q)
                    break 
        return ans 
sol = Solution()
queries = ["word","note","ants","wood"]
dictionary = ["wood","joke","moat"]
print(sol.twoEditWords(queries, dictionary))