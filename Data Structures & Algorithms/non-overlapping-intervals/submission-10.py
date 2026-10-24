class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        intervals.sort()
        print(intervals)
        candidate = intervals[0]
        count = 0
        for i in range(1, len(intervals)):
            #there is an overlap and we need to remove an interval
            # print(f'processing interval {intervals[i]} and candidate {candidate}')
            if intervals[i][0] < candidate[1]:
                count+=1
                #remove interval i
                if intervals[i][1] > candidate[1]:
                    # print(f'removing intervals {intervals[i]}')
                    continue
                else:
                    candidate = intervals[i]
                    # print(f'updating candidate {intervals[i]}')
            else:
                candidate = intervals[i]
                # print(f'outer updating candidate {intervals[i]}')
                
        return count


