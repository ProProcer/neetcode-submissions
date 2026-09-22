import heapq
class KthLargest:

    def __init__(self, k: int, nums: List[int]):
        self.nums = sorted(nums)[-k:]
        heapq.heapify(self.nums)
        self.k = k
    def add(self, val: int) -> int:
        if len(self.nums) < self.k:
            heapq.heappush(self.nums, val)
        elif self.nums[0] < val:
            heapq.heappop(self.nums)
            heapq.heappush(self.nums, val)
        return self.nums[0]
