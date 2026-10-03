"""
Definition of Interval:
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""

class Solution:
    def minMeetingRooms(self, intervals: List[Interval]) -> int:
        if not intervals:
            return 0
        result = 1
        intervals.sort(key = lambda x:x.start)
        q = deque()
        q.append(intervals[0].end)
        min_heap = [intervals[0].end]
        heapq.heapify(min_heap)
        
        
        for i in range(1, len(intervals)):
            second = intervals[i]
            
            heapq.heappush(min_heap,intervals[i].end)
            
            if second.start < min_heap[0]:
                result+=1
            else:
                heapq.heappop(min_heap)
        return result