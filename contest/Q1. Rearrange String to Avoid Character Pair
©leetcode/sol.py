class Solution:
    def rearrangeString(self, s: str, x: str, y: str) -> str:
        xCount = 0
        yCount = 0
        for c in s:
            xCount += (x == c)
            yCount += (y == c)
        