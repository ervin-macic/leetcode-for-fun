import heapq

class MedianFinder:
    def __init__(self):
        self.lower = []  # max-heap (invert values for heapq)
        self.upper = []  # min-heap

    def add_num(self, num: int) -> None:
        # Step 1: Push into max-heap (lower half)
        heapq.heappush(self.lower, -num)

        # Step 2: Ensure ordering property (max of lower <= min of upper)
        if self.upper and -self.lower[0] > self.upper[0]:
            val = -heapq.heappop(self.lower)
            heapq.heappush(self.upper, val)

        # Step 3: Rebalance sizes
        if len(self.lower) > len(self.upper) + 1:
            val = -heapq.heappop(self.lower)
            heapq.heappush(self.upper, val)
        elif len(self.upper) > len(self.lower):
            val = heapq.heappop(self.upper)
            heapq.heappush(self.lower, -val)

    def find_median(self) -> float:
        if len(self.lower) > len(self.upper):
            return -self.lower[0]
        else:
            return (-self.lower[0] + self.upper[0]) / 2


# Example usage
mf = MedianFinder()
for num in [5, 2, 8, 10, 3]:
    mf.add_num(num)
    print("Current median:", mf.find_median())
