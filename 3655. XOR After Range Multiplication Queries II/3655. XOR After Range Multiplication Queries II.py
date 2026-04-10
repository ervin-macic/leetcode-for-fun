from typing import List
class Solution:
    def xorAfterQueries(self, nums: List[int], queries: List[List[int]]) -> int:
        MOD = 1000000007
        n = len(nums)
        limit = int(n ** 0.5)
        stepBuckets = {}
        for q in queries:
            l, r, step, mul = q

            if step >= limit:
                i = l
                while i <= r:
                    nums[i] = (nums[i] * mul) % MOD
                    i += step
            else:
                if step not in stepBuckets:
                    stepBuckets[step] = []
                stepBuckets[step].append((l, r, mul))

        for step in stepBuckets:

            multiplier = [1] * (n + limit)

            for l, r, mul in stepBuckets[step]:

                multiplier[l] = (multiplier[l] * mul) % MOD

                end = l + ( (r - l) // step + 1 ) * step
                inv = pow(mul, MOD - 2, MOD)

                multiplier[end] = (multiplier[end] * inv) % MOD

            idx = step
            while idx < n:
                multiplier[idx] = (multiplier[idx] * multiplier[idx - step]) % MOD
                idx += 1

            for i in range(n):
                nums[i] = (nums[i] * multiplier[i]) % MOD

        xor_val = 0
        for val in nums:
            xor_val ^= val

        return xor_val