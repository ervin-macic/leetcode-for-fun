from sortedcontainers import SortedList
import math
class Solution:
    def maxPower(self, stations: list[int], r: int, k: int) -> int:
        n = len(stations)
        cum_sum = [0] * (n + 1)
        for i in range(n):
            cum_sum[i + 1] = cum_sum[i] + stations[i]
        
        power = [0] * n
        min_elem = 10**12
        max_elem = -1
        for i in range(n):
            left = max(0, i - r)
            right = min(n, i + r + 1)
            power[i] = cum_sum[right] - cum_sum[left]
            if power[i] < min_elem:
                min_elem = power[i]
            if power[i] > max_elem:
                max_elem = power[i]
        
        def is_target_achievable(power, k, r, target):
            spent = 0
            increases = [0] * (n+1)
            prev_added = 0
            for i in range(n):
                prev_added += increases[i]
                p = power[i] + prev_added
                if p < target:
                    last_idx_increased = i+2*r
                    by_how_much = target-p
                    prev_added += by_how_much
                    spent += by_how_much
                    if spent > k:
                        return False
                    pos = min(i+r,n-1)
                    if pos+r+1 < n:
                        increases[pos+r+1] -= by_how_much 
            if spent <= k:
                return True
            return False
        
        left = min_elem 
        right = (max_elem + k)
        while left < right:
            target = (right-left)//2 + left + 1
            if is_target_achievable(power, k, r, target):
                left = target
            else:
                right = target - 1
        return left

sol = Solution()
stations = [1,2,4,5,0]
r = 1
k = 2
stations1 = [4,4,4,4]
r1 = 0
k1 = 3
print(sol.maxPower(stations, r, k))
