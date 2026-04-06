from typing import List
from collections import defaultdict
class Solution:
    def robotSim(self, commands: List[int], obstacles: List[List[int]]) -> int:
        # -2 turn left 90
        # -1 turn right 90
        dir = 0
        dir_to_pair = [(0,1),(1,0),(0,-1),(-1,0)]
        x, y = 0, 0
        obstacles_set = set(map(tuple, obstacles))
        
        max_dist = -float("inf")
        for cmd in commands:
            if cmd == -2:
                dir -= 1
                dir %= 4
            elif cmd == -1:
                dir += 1
                dir %= 4
            else:
                dx, dy = dir_to_pair[dir]
                i = 0
                while i < cmd and (x+dx, y+dy) not in obstacles_set:
                    i += 1
                    x += dx 
                    y += dy
                max_dist = max(max_dist, x*x + y*y)
        return max_dist

sol = Solution()
commands = [6,-1,-1,6]
obstacles = [[0,0]]
print(sol.robotSim(commands, obstacles))
            