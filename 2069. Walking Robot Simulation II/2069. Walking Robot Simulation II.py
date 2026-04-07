from typing import List
class Robot:
    DIR = {
        0: "East",
        1: "South",
        2: "West",
        3: "North",
    }
    dir_to_pair = [(1,0), (0,-1), (-1,0), (0,1)]

    def __init__(self, width: int, height: int):
        self.width = width
        self.height = height
        self.x = 0
        self.y = 0
        self.dir = 0

    '''
    return: distance from robot position to edge in direction self.dir
    '''
    def get_dist(self) -> int:
        if self.dir == 0: # East
            return (self.width - 1, self.y), (self.width - 1 - self.x)
        elif self.dir == 1: # South
            return (self.x, 0), (self.y)
        elif self.dir == 2: # West 
            return (0, self.y), (self.x)
        else: # North
            return (self.x, self.height - 1), (self.height - 1 - self.y)
    
    def step(self, num: int) -> None:
        perim = 2 * (self.width + self.height - 2)
        num %= perim
        if num == 0:
            num = perim

        dx, dy = self.dir_to_pair[self.dir]

        if 0 <= self.x + num * dx < self.width and 0 <= self.y + num * dy < self.height:
            self.x += num * dx
            self.y += num * dy
        else:
            (self.x, self.y), d = self.get_dist()
            self.dir = (self.dir - 1) % 4
            num -= d
            self.step(num)

    def getPos(self) -> List[int]:
        return [self.x, self.y]

    def getDir(self) -> str:
        return self.DIR[self.dir]

width = 6 
height = 3 
obj = Robot(width, height)
obj.step(2)
obj.step(2)
print(obj.getPos())
print(obj.getDir())
obj.step(2)
obj.step(1)
obj.step(4)
print(obj.getPos())
print(obj.getDir())