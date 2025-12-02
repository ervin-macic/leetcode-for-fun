from typing import List 
MOD = 10**9+7
class Solution:
    
    def binomial(self, n, k):
        if k < 0 or k > n:
            return 0
        k = min(k, n - k)
        result = 1
        for i in range(1, k + 1):
            result = result * (n - i + 1) // i
        return result

    def countTrapezoids(self, points: List[List[int]]) -> int:
        # Sort by y coordinate
        points = sorted([y for [x,y] in points])
        const_y_segment = 1
        
        if points[0] == points[-1]:
            return 0

        y_segments = []
        for i in range(1, len(points)):
            if points[i] != points[i-1]:
                y_segments.append(const_y_segment)
                const_y_segment = 1
            else:
                const_y_segment += 1
        y_segments.append(const_y_segment)

        non_signular_y_segments = [s for s in y_segments if s != 1]
        t = len(non_signular_y_segments)

        binomials = [self.binomial(non_signular_y_segments[i], 2) % MOD for i in range(t)]
        sum_binomials = sum(binomials) % MOD
        
        sum_squared_binomials = 0
        for b in binomials:
            sum_squared_binomials = (sum_squared_binomials + b * b) % MOD
            
        inv2 = pow(2, MOD-2, MOD)
        ans = (sum_binomials * sum_binomials - sum_squared_binomials) % MOD
        ans = ans * inv2 % MOD
        return ans

sol = Solution()
points = [[1,0],[2,0],[3,0],[2,2],[3,2]]
# points = [[54,91],[-37,91],[-6,91],[-33,91]]
# points = [[30,-77],[-99,62],[14,-77],[-96,-77]]
# points = [[-73,-72],[-1,-56],[-92,30],[-57,-89],[-19,-89],[-35,30],[64,-72]]
print(sol.countTrapezoids(points))
            
