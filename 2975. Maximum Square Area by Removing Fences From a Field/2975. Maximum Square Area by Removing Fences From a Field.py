class Solution:
    def maximizeSquareArea(self, m: int, n: int, hFences: List[int], vFences: List[int]) -> int:
        MOD = 10**9 + 7
        hFences = [1] + hFences + [m]
        vFences = [1] + vFences + [n]
        h_distances = set()
        max_common = 0
        for i in range(len(hFences)):
            for j in range(i+1, len(hFences)):
                h_distances.add(abs(hFences[j] - hFences[i]))
        
        for i in range(len(vFences)):
            for j in range(i+1, len(vFences)):
                d = abs(vFences[j] - vFences[i])
                if d in h_distances:
                    max_common = max(max_common, d)
        if max_common == 0:
            return -1
        return (max_common * max_common) % MOD
        
