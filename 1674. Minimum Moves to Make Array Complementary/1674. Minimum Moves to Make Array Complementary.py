from typing import List 
class Solution:
    def minMoves(self, nums: List[int], limit: int) -> int:
        n = len(nums)
        diff = [0 for _ in range(2 * limit + 2)]
        for i in range(n // 2):
            m, M = min(nums[i], nums[~i]), max(nums[i], nums[~i])
            # key question: given a target value x, how does the number of operations required to make nums[i] + nums[~i] = x change as x varies 
            # in its natural bounds?
            # for x <= m we need 2 moves, for m < x < m+M we need 1 move, for m+M < x <= M + limit need 1 move, for M+limit < x <= 2 limit 2 moves
            diff[2] += 2
            diff[m + 1] -= 1
            diff[m + M] -= 1
            diff[m + M + 1] += 1
            diff[M + limit + 1] += 1
        ans = 10**10
        curr = 0
        for x in range(2, 2*limit+1):
            curr += diff[x]
            ans = min(ans, curr)
        return ans 