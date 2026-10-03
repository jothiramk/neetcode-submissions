class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        intervals.sort()
        result = 0
                #[[1,2],[1,4],[2,4]
        first = intervals[0]
        print(intervals)
        for i in range(1, len(intervals)):
            
            second = intervals[i]
            # print(f'first is {first} and second is {second}')
            #there is an interval
            if second[0] < first[1]:
                result+=1
                
                if second[1] > first[1]:
                    # print(f'there an overlap and ill skip the second element')
                    continue
                else:
                    # print(f'there an overlap and ill skip the first element')
                    first = second
            else:
                first = second
                
        
        return result
