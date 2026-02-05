import heapq
class MedianFinder:
    def __init__(self):
        max_heap = []
        min_heap = []

    def addNum(self, num: int) -> None:
        if not max_heap or num <= max_heap.top():
            # push number to max heap of lower half of numbers
        else: 
            # push number to min heap of upper half of numbers
        # Balance heaps if necessary
        if max_heap.size() > min_heap.size() + 1:
            # push max_heap.top into min_heap
        if min_heap.size() > max_heap.size() + 1:
            # push min_heap.top into max_heap

    def findMedian(self) -> float:
        n = max_heap.size() + min_heap.size()
        if max_heap.size() == n/2:
            return max_heap.top()
        else:
            return min_heap.top()

# Your MedianFinder object will be instantiated and called as such:
# obj = MedianFinder()
# obj.addNum(num)
# param_2 = obj.findMedian()