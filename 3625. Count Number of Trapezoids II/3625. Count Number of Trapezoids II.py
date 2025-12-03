from math import gcd
from collections import defaultdict
from typing import List

class Solution:
    def countTrapezoids(self, points: List[List[int]]) -> int:
        n = len(points)
        inf = 10**9 + 7
        # For all segments with the same slope, which are collinear? the ones with the same intercepts
        slope_to_intercept = defaultdict(list)
        # If two segments share a midpoint, then we've got a parallelogram issue
        # If n segments share a midpoint, then we've got nC2 parallelograms overcounted
        mid_to_slope = defaultdict(list)
        ans = 0
        
        for i in range(n):
            x1, y1 = points[i]
            for j in range(i+1, n):
                x2, y2 = points[j]
                
                dx = x1 - x2
                dy = y1 - y2
                
                intercept = 0
                if dx == 0:
                    slope = inf
                    intercept = x1
                else:
                    slope = (y2 - y1) / (x2 - x1)
                    intercept = (y1 * dx - x1 * dy) / dx 

                # mid = ((x1+x2)/2, (y1+y2)/2) won't work bc of float representation equality comparison
                # hopefully a linear combination of the sum of coordinates is a hash map essentially.
                whatever1 = 10000
                whatever2 = 1
                mid = (x1 + x2) * whatever1 + (y1 + y2) * whatever2

                slope_to_intercept[slope].append(intercept)
                mid_to_slope[mid].append(slope)
        
        # Solve 3623 basically:
        # For each slope, calculate contribution to ans
        for s_to_i in slope_to_intercept.values():
            # Only one line segment on this particular slope (no corresponding sloped base so no trapezoids unfortunately)
            if len(s_to_i) == 1:
                continue
            
            # Count how many points we have at this slope at this particular intercept
            cnt = defaultdict(int)
            for intercept in s_to_i:
                cnt[intercept] += 1

            # Calculate contribution to ans
            total_sum = 0
            for count in cnt.values():
                ans += total_sum * count
                total_sum += count
        
        # Remove double counted parallelograms:
        for m_to_s in mid_to_slope.values():
            # If only one slope passing through this mid, no parallelograms here
            if len(m_to_s) == 1:
                continue
            
            # Count how many lines pass through the same midpoint
            cnt = defaultdict(int)
            # This midpoint is the linear combination of the coordinates, not the actual midpoint
            for midpoint in m_to_s:
                cnt[midpoint] += 1

            total_sum = 0
            for count in cnt.values():
                ans -= total_sum * count
                total_sum += count

        return ans
