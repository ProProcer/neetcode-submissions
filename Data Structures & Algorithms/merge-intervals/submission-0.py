class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        if len(intervals) == 0:
            return intervals
        intervals.sort()
        i = 1
        while i < len(intervals):
            curr = intervals[i]
            prev = intervals[i - 1]
            if curr[0] <= prev[1] and curr[1] >= prev[0]:
                intervals[i -1] = [prev[0], max(prev[1], curr[1])]
                intervals.pop(i)
            else:
                i += 1
        return intervals