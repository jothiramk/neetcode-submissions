"""
Definition of Interval:
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""

class Solution:
    def canAttendMeetings(self, intervals: List[Interval]) -> bool:
        intervals.sort(key = lambda x : x.start)
        if not intervals:
            return True
        first = intervals[0]
        for i in range(1,len(intervals)):
            second = intervals[i]
            if second.start < first.end:
                return False
            else:
                first = second
        
        return True
