from typing import List
class Solution:
    def areSimilar(self, mat: List[List[int]], k: int) -> bool:
        m = len(mat)
        n = len(mat[0])
        for i in range(m):
            if i % 2 == 0:
                # even case, compare a[i+k] with a[i]
                for j in range(n):
                    if mat[i][j] != mat[i][(j+k) % n]:
                        return False
            else:
                # odd case, compare a[i-k] with a[i]
                for j in range(n):
                    if mat[i][j] != mat[i][(j-k) % n]:
                        return False
        return True
sol = Solution()
mat = [[1,2,3],[4,5,6],[7,8,9]]
k = 4
mat = [[1,2,1,2],[5,5,5,5],[6,3,6,3]]
k = 2
print(sol.areSimilar(mat, k))