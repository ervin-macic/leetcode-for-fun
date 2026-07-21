class Node:
    def __init__(self, val=None, minVal=None, nextNode=None):
        self.val = val 
        self.min = minVal
        self.next = nextNode

class MinStack:
    def __init__(self):
        self.stack = None

    def push(self, value: int) -> None:
        if not self.stack:
            self.stack = Node(value, value, None)
        else:
            self.stack = Node(value, min(value, self.stack.min), self.stack)

    def pop(self) -> None:
        self.stack = self.stack.next

    def top(self) -> int:
        return self.stack.val

    def getMin(self) -> int:
        return self.stack.min

# Your MinStack object will be instantiated and called as such:
value = 50
obj = MinStack()
obj.push(value)
obj.pop()
param_3 = obj.top()
param_4 = obj.getMin()