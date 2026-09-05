from collections import defaultdict
import heapq
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        counts = defaultdict(int)
        for n in nums:
            counts[n] += 1
        
        myheap = []
        for key, val in counts.items():
            heapq.heappush(myheap, (val, key))
            if len(myheap) > k:
                heapq.heappop(myheap)
        result = []
        for i in range(len(myheap)):
            result.append(heapq.heappop(myheap)[1])
        return result