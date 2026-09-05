from collections import defaultdict
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        counts = defaultdict(int)
        for n in nums:
            counts[n] += 1

        top = sorted(counts.keys(), reverse = True, key = lambda x : counts[x])
        return top[0:k]