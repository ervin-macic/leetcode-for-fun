from collections import Counter

class Solution:
    def topKFrequent(self, nums, k):
        freq = Counter(nums)

        buckets = [[] for _ in range(len(nums) + 1)]

        for num, f in freq.items():
            buckets[f].append(num)

        result = []

        for f in range(len(nums), 0, -1):
            for num in buckets[f]:
                result.append(num)
                if len(result) == k:
                    return result