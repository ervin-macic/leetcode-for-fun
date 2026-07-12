class Solution:
    def arrayRankTransform(self, arr: List[int]) -> List[int]:
        rank = {}
        currRank = 1
        for x in sorted(set(arr)):
            rank[x] = currRank
            currRank += 1
        return [rank[x] for x in arr]
