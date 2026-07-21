class MyQueue:

    def __init__(self):
        self.enq = []
        self.deq = []
        self.front = None

    def push(self, x: int) -> None:
        self.enq.append(x)
    
    def pop(self) -> int:
        if len(self.deq) == 0:
            self.enqToDeq()
        return self.deq.pop()

    def enqToDeq(self) -> None:
        while self.enq:
            top = self.enq.pop()
            self.deq.append(top)
        
    def peek(self) -> int:
        if len(self.deq) == 0:
            self.enqToDeq()
        return self.deq[-1]
    
    def empty(self) -> bool:
        return not self.enq and not self.deq

# Your MyQueue object will be instantiated and called as such:
# obj = MyQueue()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.peek()
# param_4 = obj.empty()