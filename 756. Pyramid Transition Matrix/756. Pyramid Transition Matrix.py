from typing import List
from collections import defaultdict
class Solution:
    def pyramidTransition(self, bottom: str, allowed: List[str]) -> bool:
        n = len(bottom)
        # Construct pyramid
        pyramid = [['.' for _ in range(k)] for k in range(1, n+1)]
        for i in range(n):
            pyramid[-1][i] = bottom[i]
        
        # Process options
        options = defaultdict(list)
        for x,y,z in allowed:
            options[(x,y)].append(z)
        
        # Main backtracking function
        def backtrack(row: int, col: int, pyramid: List[List[chr]]):
            children = (pyramid[row+1][col], pyramid[row+1][col+1])
            if row == 0:
                if options[children]:
                    return True 
                return False
            
            for option in options[children]:
                pyramid[row][col] = option

                # What's the next [row][col] to set?
                if col == row:
                    next_row = row - 1
                    next_col = 0
                else:
                    next_row = row
                    next_col = col + 1
                
                # Is it possible to finish when choosing this option given what we've built so far?
                if backtrack(next_row, next_col, pyramid):
                    return True
            return False
        
        return backtrack(n-2, 0, pyramid)
    
sol = Solution()
bottom = "AAAA"
allowed = ["AAB","AAC","BCD","BBE","DEF"]
print(sol.pyramidTransition(bottom, allowed))