"""
Definition of Interval:
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""

class Solution:
    def minMeetingRooms(self, intervals: List[Interval]) -> int:
        intervals.sort(key = lambda x:x.start)
        # print(intervals)
        #create a min heap with the end times
        min_heap = []
        rooms = 0
        for interval in intervals:
            room_reused = False
            # print(f'processing start in {interval.start} and {interval.end}')
            # if the the room is avaiable, update the min heap. i.e no new room required
            if min_heap and min_heap[0] <= interval.start:    
                heapq.heappop(min_heap)
            else:
                rooms+=1
            heapq.heappush(min_heap,interval.end)
            
                
                
        
        return rooms
    