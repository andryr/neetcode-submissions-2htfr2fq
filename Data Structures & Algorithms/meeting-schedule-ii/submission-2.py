"""
Definition of Interval:
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""

class Solution:
    def minMeetingRooms(self, intervals: List[Interval]) -> int:
        ans = 0
        rooms = 0
        bounds = [(i.start, True) for i in intervals] + [(i.end, False) for i in intervals]
        bounds.sort()
        for bound, is_start in bounds:
            if is_start:
                rooms += 1
            else:
                rooms -= 1
            ans = max(rooms, ans)
        return ans