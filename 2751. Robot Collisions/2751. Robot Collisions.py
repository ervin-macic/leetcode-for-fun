from typing import List
from dataclasses import dataclass

@dataclass
class Robot:
    position: int
    health: int
    direction: str
    idx: int

class Solution:
    def survivedRobotsHealths(self, positions: List[int], healths: List[int], directions: str) -> List[int]:
        robots = sorted([Robot(p, h, d, i) for i, (p, h, d) in enumerate(zip(positions, healths, directions))], key = lambda r: r.position)
        stack = []
        survivors = []

        for robot in robots:
            if robot.direction == 'R':
                stack.append(robot)
            else:
                while stack:
                    top = stack[-1]
                    if top.health > robot.health:
                        top.health -= 1
                        robot = None
                        break
                    elif top.health < robot.health:
                        robot.health -= 1
                        stack.pop()
                    else:
                        # both die when equal health level
                        stack.pop()
                        robot = None
                        break
                if robot:
                    survivors.append(robot)

        result = stack + survivors
        result.sort(key = lambda r: r.idx)
        return [r.health for r in result]

sol = Solution()
positions = [3,5,2,6]
healths = [10,10,15,12]
directions = "RLRL"
print(sol.survivedRobotsHealths(positions, healths, directions))