import heapq

class MedianFinder:

    def __init__(self):
        self.l_heap = list()
        self.r_heap = list()

    def addNum(self, num: int) -> None:
        if len(self.l_heap) and num >= -self.l_heap[0]:
            heapq.heappush(self.r_heap, num)
        else:
            heapq.heappush(self.l_heap, -num)
        while len(self.l_heap) > len(self.r_heap):
            heapq.heappush(self.r_heap, -heapq.heappop(self.l_heap))
        if len(self.r_heap) > len(self.l_heap):
            heapq.heappush(self.l_heap, -heapq.heappop(self.r_heap))

    def findMedian(self) -> float:
        if len(self.l_heap) == len(self.r_heap):
            return (-self.l_heap[0] + self.r_heap[0]) / 2
        return -self.l_heap[0]


# Your MedianFinder object will be instantiated and called as such:
# obj = MedianFinder()
# obj.addNum(num)
# param_2 = obj.findMedian()