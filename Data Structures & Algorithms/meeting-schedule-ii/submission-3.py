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
        
        intervals.sort(key=lambda x:x.start)
        #create a min heap on the end times
        minHeap = []
        rooms = 1
        heapq.heappush(minHeap,intervals[0].end)
    
        for i in range(1,len(intervals)):
            start , end = intervals[i].start,intervals[i].end 
            if start < minHeap[0]:
                rooms += 1
            else:
                heapq.heappop(minHeap)
            heapq.heappush(minHeap,end)
            

        
        return rooms
