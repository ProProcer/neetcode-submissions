class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:

        for i in range(len(intervals)):
            curr_interval = intervals[i]
            if newInterval[1] >= curr_interval[0] and newInterval[0] <= curr_interval[1]:
                curr_interval = newInterval
                while i < len(intervals):
                    next_interval = intervals[i]
                    if not( next_interval[1] >= curr_interval[0] and next_interval[0] <= curr_interval[1]):
                        break
                    curr_interval = [
                        min(curr_interval[0], next_interval[0]), 
                        max(curr_interval[1], next_interval[1])
                    ]
                    intervals.pop(i)

                    
                intervals.insert(i, curr_interval)
                return intervals
            if newInterval[0] < curr_interval[0]:
                intervals.insert(i, newInterval)
                return intervals
        intervals.append(newInterval)
        return intervals
