from collections import defaultdict
from sortedcontainers import Sort
class Solution:
    def findDifferentBinaryString(self, nums: list[str]) -> str:
        n = len(nums)
        d = defaultdict(bool)
        for s in nums:
            d[int(s, 2)] = True 
        for i in range(1 << n):
            if not d[i]:
                return bin(i)[2:].zfill(n)