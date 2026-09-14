class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        removed = 0
        intervals.sort(key = lambda x : x[1])
        prev = intervals[0]
        for i in range(1, len(intervals)):
            curr = intervals[i]
            if curr[0] < prev[1]:
                removed += 1
            else:
                prev = curr
        return removed