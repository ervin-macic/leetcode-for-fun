class Solution:
    def maxDistance(self, colors: list[int]) -> int:
        n = len(colors)
        # include leftmost
        r = n - 1
        while colors[r] == colors[0]:
            r -= 1
        # include rightmost
        l = 0
        while colors[l] == colors[-1]:
            l += 1
        return max(r, n - 1 - l)