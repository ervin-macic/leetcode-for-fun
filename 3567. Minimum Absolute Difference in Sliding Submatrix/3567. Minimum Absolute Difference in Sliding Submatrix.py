class Solution:
    def minAbsDiff(self, grid: List[List[int]], k: int) -> List[List[int]]:
        m = len(grid)
        n = len(grid[0])

        def getMinAbsDiff(lst: list[int]):
            lst = sorted(set(lst))
            if len(lst) < 2:
                return 0
            ans = float("inf")
            for x, y in zip(lst, lst[1:]):
                ans = min(ans, y - x)
            return ans

        ans = [[0 for _ in range(n - k + 1)] for _ in range(m - k + 1)]

        for i in range(m - k + 1):
            for j in range(n - k + 1):
                lst = []
                for r in range(i, i + k):
                    lst += grid[r][j:j + k]
                ans[i][j] = getMinAbsDiff(lst)

        return ans