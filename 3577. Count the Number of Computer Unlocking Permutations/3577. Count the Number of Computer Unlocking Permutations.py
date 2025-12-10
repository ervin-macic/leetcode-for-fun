class Solution:
    def countPermutations(self, complexity: List[int]) -> int:
        n = len(complexity)
        mini = MOD = 10**9 + 7
        # check unique minimum
        cnt = 0
        for c in complexity:
            if c <= mini:
                mini = c
                cnt += 1
            if cnt > 1:
                return 0
        if mini != complexity[0]:
            return 0
        ans = 1
        for i in range(2, n):
            ans = (ans * i) % MOD
        return ans