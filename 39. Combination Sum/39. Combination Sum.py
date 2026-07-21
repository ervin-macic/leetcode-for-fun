from typing import List
class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        candidates.sort()
        n = len(candidates)
        ans = []
        def solve(i, curr: List[int], currSum):
            nonlocal n 
            if currSum == target:
                ans.append(curr.copy())
                return
            while i < n and currSum + candidates[i] <= target:
                curr.append(candidates[i])
                solve(i, curr, currSum + candidates[i])
                curr.pop()
                i += 1
            return 
        for i in range(n):
            if candidates[i] > target:
                break
            solve(i, [candidates[i]], candidates[i])
        return ans
sol = Solution()
candidates = [2,3,6,7]
target = 7
print(sol.combinationSum(candidates, target))
