from bisect import bisect_right
class TimeMap:

    def __init__(self):
        self.d = {}
        
    def set(self, key: str, value: str, timestamp: int) -> None:
        if not key in self.d:
            self.d[key] = []
        self.d[key].append((timestamp, value))

    def get(self, key: str, timestamp: int) -> str:
        if key not in self.d:
            return ""
        idx = bisect_right(self.d[key], timestamp, key=lambda p: p[0])
        if idx == 0:
            return ""
        return self.d[key][idx-1][1]


# Your TimeMap object will be instantiated and called as such:
obj = TimeMap()
key = "abc"
value = 10
timestamp = 5
obj.set(key,value,timestamp)
obj.set(key, 12, 6)
obj.set(key, 20, 3)

param_2 = obj.get(key, 7)
print(param_2)
