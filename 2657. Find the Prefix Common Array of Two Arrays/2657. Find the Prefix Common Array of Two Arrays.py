from typing import List
class Solution:
    def findThePrefixCommonArray(self, A: List[int], B: List[int]) -> List[int]:
        n = len(A)
        C = [0] * n 
        seen_in_A = [False] * (n+1)
        seen_in_B = [False] * (n+1)
        if A[0] == B[0]:
            C[0] = 1
        seen_in_A[A[0]] = seen_in_B[B[0]] = True
        for i in range(1, n):
            C[i] = C[i-1]
            if A[i] == B[i]:
                C[i] += 1 
            else:
                if seen_in_A[B[i]]:
                    if seen_in_B[A[i]]:
                        C[i] += 2
                    else:
                        C[i] += 1
                elif seen_in_B[A[i]]:
                    C[i] += 1
            seen_in_A[A[i]] = seen_in_B[B[i]] = True 
        return C 
sol = Solution()
A = [1,3,2,4]
B = [3,1,2,4]
A = [2,3,1]
B = [3,1,2]
print(sol.findThePrefixCommonArray(A,B))

            