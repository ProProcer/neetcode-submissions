from collections import defaultdict
import heapq
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        counts = defaultdict(int)
        for n in nums:
            counts[n] += 1
        
        myheap = [(-v, k) for k, v in counts.items()]
        heapq.heapify(myheap)
        result = []
        for i in range(k):
            result.append(heapq.heappop(myheap)[1])
        return result