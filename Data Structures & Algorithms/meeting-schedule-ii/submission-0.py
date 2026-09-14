"""
Definition of Interval:
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""

class Solution:
    def minMeetingRooms(self, intervals: List[Interval]) -> int:
        starts = sorted(x.start for x in intervals)
        ends = sorted(x.end for x in intervals)

        start_ptr = 0
        end_ptr = 0
        max_room = 0
        curr_room = 0
        while start_ptr < len(starts):
            if starts[start_ptr] < ends[end_ptr]:
                curr_room += 1
                max_room = max(curr_room, max_room)
                start_ptr += 1
            else:
                curr_room -= 1
                end_ptr += 1
        return max_room