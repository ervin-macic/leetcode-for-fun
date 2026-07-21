class MyQueue:

    def __init__(self):
        self.enq = []
        self.deq = []
        self.front = None

    def push(self, x: int) -> None:
        if self.front is None:
            self.front = x
        if self.deq:
            self.deqToEnq()
        self.enq.append(x)

    def pop(self) -> int:
        if self.enq:
            self.enqToDeq()
        top = self.deq.pop()
        if self.deq:
            self.front = self.deq[-1]
        else:
            self.front = None
        return top

    def enqToDeq(self) -> None:
        while self.enq:
            top = self.enq.pop()
            self.deq.append(top)
        
    def deqToEnq(self) -> None:
        while self.deq:
            top = self.deq.pop()
            self.enq.append(top)
        
    def peek(self) -> int:
        if self.front is not None:
            return self.front
        if self.enq:
            self.enqToDeq()
        self.front = self.deq[-1]
        return self.deq[-1]
        
    def empty(self) -> bool:
        return not self.enq and not self.deq

# Your MyQueue object will be instantiated and called as such:
# obj = MyQueue()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.peek()
# param_4 = obj.empty()