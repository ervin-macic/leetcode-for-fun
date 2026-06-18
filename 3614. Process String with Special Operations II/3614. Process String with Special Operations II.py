class Solution:
    def processStr(self, s: str, k: int) -> str:
        n = 0
        for ch in s:
            if ch == "*":
                n = max(0, n - 1)
            elif ch == "#":
                n *= 2
            elif ch != "%":
                n += 1

        if k >= n:
            return "."

        for ch in reversed(s):
            if ch == "*":
                n += 1

            elif ch == "#":
                half = n // 2
                if k >= half:
                    k -= half
                n = half

            elif ch == "%":
                k = n - 1 - k

            else:
                if k == n - 1:
                    return ch
                n -= 1

        return "."