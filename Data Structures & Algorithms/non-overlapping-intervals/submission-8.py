class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        intervals.sort()
        result = 0
        first = intervals[0]
        # print(intervals)
        for i in range(1, len(intervals)):
            second = intervals[i]
            #there is an interval
            if second[0] < first[1]:
                result+=1
                if second[1] > first[1]:
                    continue
                else:
                    first = second
            else:
                first = second
        return result


