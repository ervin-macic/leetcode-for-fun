from math import pi
class Solution:
    def angleClock(self, hour: int, minutes: int) -> float:
        hour %= 12
        arg_mins = 2 * pi * minutes / 60 
        arg_hours = 2 * pi / 12 * (hour + minutes / 60)
        delta = abs(arg_hours - arg_mins)
        ans = min(delta, 2 * pi - delta)
        return (360 * ans) / (2 * pi)