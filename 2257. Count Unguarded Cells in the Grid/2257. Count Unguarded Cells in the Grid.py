from collections import defaultdict
from typing import Literal
class Solution:
    def countUnguarded(self, m: int, n: int, guards: list[list[int]], walls: list[list[int]]) -> int:
        guarded = defaultdict(bool)
        wall_dict = defaultdict(bool)
        for [x,y] in walls:
            wall_dict[(x,y)] = True 
        guard_dict = defaultdict(bool)
        for [x,y] in guards:
            guard_dict[(x,y)] = True 
        num_guarded = 0
        Object = Literal['W', 'G']
        # Scan West - East
        for i in range(0, m):
            last_seen : Object = 'W'
            for j in range(0, n):
                if wall_dict[(i,j)]:
                    last_seen = 'W'
                elif guard_dict[(i,j)]:
                    last_seen = 'G'
                    if not guarded[(i,j)]:
                        guarded[(i,j)] = True
                        num_guarded += 1
                else:
                    if last_seen == 'G' and not guarded[(i,j)]:
                        guarded[(i,j)] = True
                        num_guarded += 1 
        # Scan East - West
        for i in range(0, m):
            last_seen : Object = 'W'
            for j in range(n-1, -1, -1):
                if wall_dict[(i,j)]:
                    last_seen = 'W'
                elif guard_dict[(i,j)]:
                    last_seen = 'G'
                    if not guarded[(i,j)]:
                        guarded[(i,j)] = True
                        num_guarded += 1
                else:
                    if last_seen == 'G' and not guarded[(i,j)]:
                        guarded[(i,j)] = True 
                        num_guarded += 1
        # Scan North - South
        for j in range(0, n):
            last_seen : Object = 'W'
            for i in range(0, m):
                if wall_dict[(i,j)]:
                    last_seen = 'W'
                elif guard_dict[(i,j)]:
                    last_seen = 'G'
                    if not guarded[(i,j)]:
                        guarded[(i,j)] = True
                        num_guarded += 1
                else:
                    if last_seen == 'G' and not guarded[(i,j)]:
                        guarded[(i,j)] = True
                        num_guarded += 1
        # Scan South - North
        for j in range(0, n):
            last_seen : Object = 'W'
            for i in range(m-1, -1, -1):
                if wall_dict[(i,j)]:
                    last_seen = 'W'
                elif guard_dict[(i,j)]:
                    last_seen = 'G'
                    if not guarded[(i,j)]:
                        guarded[(i,j)] = True
                        num_guarded += 1
                else:
                    if last_seen == 'G' and not guarded[(i,j)]:
                        guarded[(i,j)] = True
                        num_guarded += 1
        ans = m*n - len(walls) - num_guarded
        return ans
        
sol = Solution()
m = 4 
n = 6
guards = [[0,0],[1,1],[2,3]] 
walls = [[0,1],[2,2],[1,4]]
print(sol.countUnguarded(m,n,guards,walls))