from bisect import bisect_left

class Solution:
    def maxDistance(self, side: int, points: list[list[int]], k: int) -> int:
        n = len(points)
        line = []
        for x, y in points:
            if y == 0: line.append(x)
            elif x == side: line.append(side + y)
            elif y == side: line.append(3 * side - x)
            else: line.append(4 * side - y)
        
        line.sort()
        total_dist = 4 * side

        def is_achievable(d: int) -> bool:
            for start_idx in range(n):
                if line[start_idx] > line[0] + d: break 
                count = 1
                curr_val = line[start_idx]
                for _ in range(k-1):
                    next_pos = bisect_left(line, curr_val + d)
                    if next_pos == n:
                        break
                    curr_val = line[next_pos]
                    count += 1
                
                if count == k and (total_dist - curr_val + line[start_idx]) >= d:
                    return True
            return False
        return bisect_left(range(1, total_dist // k + 1), True, key=lambda x: not is_achievable(x))  

sol = Solution()
side = 2
points = [[0,0],[1,2],[2,0],[2,2],[2,1]]
k = 4
side = 2
points = [[0,2],[2,0],[2,2],[0,0]]
k = 4
print(sol.maxDistance(side, points, k))