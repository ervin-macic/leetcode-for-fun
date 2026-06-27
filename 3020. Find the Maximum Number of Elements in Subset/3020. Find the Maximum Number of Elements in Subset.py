from collections import defaultdict

class Solution:
    def maximumLength(self, nums: List[int]) -> int:
        d = defaultdict(int)
        for num in nums:
            d[num] += 1

        ans = 1
        if d[1]:
            ans = d[1] if d[1] % 2 else d[1] - 1
        for start in list(d.keys()):
            if start == 1:
                continue
            x = start
            curr = 0
            while d[x] >= 2:
                curr += 2
                x = x * x
            if d[x] == 1:
                curr += 1
            else:
                curr -= 1
            ans = max(ans, curr)
        return ans