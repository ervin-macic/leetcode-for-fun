from typing import List
from collections import defaultdict, deque
from math import isqrt
class Solution:
    def minJumps(self, nums: List[int]) -> int:
        n = len(nums)
        def prime(n: int) -> bool:
            if n == 1:
                return False
            if n == 2:
                return True
            if n % 2 == 0:
                return False
            for d in range(3, isqrt(n) + 1, 2):
                if n % d == 0:
                    return False
            return True
        is_prime = {x: prime(x) for x in set(nums)}

        # prime -> indices
        divisible_by = defaultdict(list)
        for i, num in enumerate(nums):
            x = num
            factors = set()
            d = 2
            while d * d <= x:
                while x % d == 0:
                    factors.add(d)
                    x //= d
                d += 1
            if x > 1:
                factors.add(x)
            for p in factors:
                divisible_by[p].append(i)
        q = deque()
        q.append(0)
        depth = [-1] * n
        depth[0] = 0
        while q:
            i = q.popleft()
            if i == n - 1:
                return depth[i]
            for nxt in (i - 1, i + 1):
                if 0 <= nxt < n and depth[nxt] == -1:
                    depth[nxt] = depth[i] + 1
                    q.append(nxt)
            val = nums[i]
            if is_prime[val]:
                for nxt in divisible_by[val]:
                    if depth[nxt] == -1:
                        depth[nxt] = depth[i] + 1
                        q.append(nxt)
                divisible_by[val].clear()
        return -1

sol = Solution()
nums = [2,3,4,7,9]
nums = [1,2,4,6]
print(sol.minJumps(nums))