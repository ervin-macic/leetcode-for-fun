from typing import List
class Solution:
    def select_ith(arr, i):
        """
        Returns the i-th smallest element (0-indexed) in arr
        using the deterministic Median-of-Medians algorithm.
        """

        # Base case: small list → sort and return
        if len(arr) <= 5:
            return sorted(arr)[i]

        # Step 1 — Split arr into groups of 5 and gather medians
        groups = [arr[j:j+5] for j in range(0, len(arr), 5)]
        medians = [sorted(group)[len(group)//2] for group in groups]

        # Step 2 — Recursively compute median of medians = pivot
        pivot = select_ith(medians, len(medians)//2)

        # Step 3 — Partition around pivot
        lows   = [x for x in arr if x < pivot]
        highs  = [x for x in arr if x > pivot]
        pivots = [x for x in arr if x == pivot]   # duplicates allowed

        # Step 4 — Recurse into the correct partition
        if i < len(lows):
            return select_ith(lows, i)
        elif i < len(lows) + len(pivots):
            return pivot
        else:
            return select_ith(highs, i - len(lows) - len(pivots))

    def maxRunTime(self, n: int, batteries: List[int]) -> int:
        batteries.sort()
        m = len(batteries)
        
        top_n = batteries[m-n:]
        excess = sum(batteries[:m-n])
        
        for i in range(n-1):
            gap = top_n[i+1] - top_n[i]
            needed = (i + 1) * gap
            
            if excess < needed:
                return top_n[i] + excess // (i + 1)
            
            excess -= needed
        
        return top_n[-1] + excess // n
    
class Solution2:
    def maxRunTime(self, n: int, batteries: List[int]) -> int:
        left, right = 0, sum(batteries) // n + 1
        while left + 1 < right:
            mid = (left + right) // 2
            sum = 0
            for b in batteries:
                sum += min(b, mid)
            if n * mid <= sum:
                left = mid
            else:
                right = mid
        return left
                
sol = Solution()
n = 2
batteries = [3,3,3]
print(sol.maxRunTime(n, batteries))