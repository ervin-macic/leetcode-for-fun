class Solution:
    def sortByBits(self, arr: list[int]) -> list[int]:
        arr.sort(key=lambda x: (x.bit_count(), x))
        return arr