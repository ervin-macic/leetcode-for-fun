def bisect_left_desc(arr, n, x):
    lo, hi = 0, n
    while lo < hi:
        mid = (lo + hi) // 2
        if arr[mid] > x:
            lo = mid + 1
        else:
            hi = mid
    return lo
class Solution:
    def countNegatives(self, grid: List[List[int]]) -> int:
        m = len(grid)
        n = len(grid[0])
        ans = 0
        curr_len = n
        for i in range(m):
            neg_idx = bisect_left_desc(grid[i], curr_len, -1)
            ans += (n - neg_idx)
            curr_len = neg_idx
        return ans
