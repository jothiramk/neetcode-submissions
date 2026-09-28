class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:

        result = []
        if not intervals :
            return [newInterval]
        new_intervals= []
        for i, interval in enumerate(intervals):
            if newInterval[0] <= interval[0]:
                new_intervals.append(newInterval)
                new_intervals.extend(intervals[i:])
                break
            else:
                new_intervals.append(interval)
        if len(new_intervals) < (len(intervals)+1):
            new_intervals.append(newInterval)
        
        # print(new_intervals)
        # intervals.append(newInterval)
        # intervals.sort(key=lambda x:x[0])

        intervals = new_intervals
        
        start_ref = intervals[0][0]
        end_ref = intervals[0][1]
        # print(f'start_ref is {start_ref} and end_ref is {end_ref}')
        for i in range(1,len(intervals)):
            start = intervals[i][0]
            end = intervals[i][1]
            # print(f'start is {start} and end is {end}')
            if start <= end_ref:
                end_ref=max(end,end_ref)
            else:
                result.append([start_ref,end_ref])
                start_ref=start
                end_ref=max(end,end_ref)
            # print(f'result is {result}')
        result.append([start_ref,end_ref])
        return result


