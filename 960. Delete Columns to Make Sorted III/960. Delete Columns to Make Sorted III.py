from typing import List
class Solution:
    def min_vertex_cover(self, edges):
        if not edges:
            return set()
        u, v = next(iter(edges))
        # Include u
        edges1 = {e for e in edges if u not in e}
        cover1 = {u} | self.min_vertex_cover(edges1)
        # Include v
        edges2 = {e for e in edges if v not in e}
        cover2 = {v} | self.min_vertex_cover(edges2)
        # Return smaller cover
        return cover1 if len(cover1) <= len(cover2) else cover2

    def minDeletionSize(self, strs: List[str]) -> int:
        n = len(strs)
        m = len(strs[0])
        inversions = set()
        for s in strs:
            for i in range(m):
                for j in range(i+1, m):
                    if s[i] > s[j]:
                        inversions.add((i,j))
        
        cover = self.min_vertex_cover(inversions)
        return len(cover)

sol = Solution()
strs = ["babca","bbazb"]
print(sol.minDeletionSize(strs))