from collections import defaultdict
class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        count_map = defaultdict(int)
        res = 0
        for n in nums: 
            if not count_map[n]:
                count_map[n] = count_map[n - 1] + count_map[n + 1] + 1
                count_map[n - count_map[n - 1]] = count_map[n]
                count_map[n + count_map[n + 1]] = count_map[n]
                res = max(res, count_map[n])
        return res