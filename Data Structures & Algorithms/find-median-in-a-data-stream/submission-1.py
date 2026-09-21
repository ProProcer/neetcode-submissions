import heapq
class MedianFinder:

    def __init__(self):
        self.left = []
        self.right = []        

    def addNum(self, num: int) -> None:
        if len(self.left) < len(self.right):
            if self.right and num > self.right[0]:
                heapq.heappush(self.right, num)
                heapq.heappush(self.left, -heapq.heappop(self.right))
            else:
                heapq.heappush(self.left, -num)
        else:
            if self.left and num < -self.left[0]:
                heapq.heappush(self.left, -num)
                heapq.heappush(self.right, -heapq.heappop(self.left))
            else:
                heapq.heappush(self.right, num)
    

    def findMedian(self) -> float:
        if (len(self.left) + len(self.right)) % 2 == 0:
            return (-self.left[0] + self.right[0]) / 2
        else:
            return self.right[0]
        