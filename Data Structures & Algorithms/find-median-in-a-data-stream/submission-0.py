import bisect
class MedianFinder:

    def __init__(self):
        self.med = None
        self.seq = []

    def addNum(self, num: int) -> None:
        bisect.insort(self.seq, num)
    def findMedian(self) -> float:
        N = len(self.seq)
        if N % 2 == 0:
            return (self.seq[N // 2 - 1] + self.seq[N // 2]) / 2
        else:
            return self.seq[N // 2]
        