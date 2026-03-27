from collections import Counter
class Solution:
    def topKFrequent(self, nums: list[int], k: int) -> list[int]:
        return [x for (x,y) in Counter(nums).most_common(k)]
            