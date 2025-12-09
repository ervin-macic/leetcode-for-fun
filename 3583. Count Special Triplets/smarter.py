class Solution:
    def specialTriplets(self, nums):
        MOD = 10**9 + 7
        n = len(nums)

        from collections import Counter

        # count occurrences on the right
        right = Counter(nums)
        left = Counter()

        total = 0

        for j, x in enumerate(nums):
            # remove current from right
            right[x] -= 1
            if right[x] == 0:
                del right[x]

            # nums[i] must be 2*x
            left_count = left[2*x]
            # nums[k] must be 2*x
            right_count = right.get(2*x, 0)

            total = (total + left_count * right_count) % MOD

            # add current to left
            left[x] += 1

        return total
