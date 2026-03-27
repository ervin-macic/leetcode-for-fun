import random

class RandomizedSet:

    def __init__(self):
        self.lst = []
        self.idx = {}

    def insert(self, val: int) -> bool:
        if val in self.idx:
            return False
        
        self.idx[val] = len(self.lst)
        self.lst.append(val)
        return True

    def remove(self, val: int) -> bool:
        if val not in self.idx:
            return False
        
        index = self.idx[val]
        last_val = self.lst[-1]

        self.lst[index] = last_val
        self.idx[last_val] = index

        self.lst.pop()
        del self.idx[val]
        
        return True

    def getRandom(self) -> int:
        return random.choice(self.lst)

obj = RandomizedSet()
param_1 = obj.insert(val)
param_2 = obj.remove(val)
param_3 = obj.getRandom()