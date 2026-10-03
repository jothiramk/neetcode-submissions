class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        # 1. Sort by END time (the game changer)
        intervals.sort(key=lambda x: x[1])
        
        result = 0
        first = intervals[0]
        
        for i in range(1, len(intervals)):
            second = intervals[i]
            
            # 2. Check for overlap
            if second[0] < first[1]:
                result += 1  # Greedily drop 'second' because it ends later than 'first'
            else:
                first = second  # No overlap, move onto tracking 'second'
                
        return result
