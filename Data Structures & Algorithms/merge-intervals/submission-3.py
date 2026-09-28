class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        res = []
        #sort the intervals
        intervals.sort(key=lambda x:x[0])

        non_merge_interval_start = intervals[0][0]
        non_merge_interval_end = intervals[0][1]
        for i in range(1, len(intervals)):
            if intervals[i][0] <= max(non_merge_interval_start,non_merge_interval_end):
                non_merge_interval_start = min(non_merge_interval_start,intervals[i][0])
                non_merge_interval_end = max(non_merge_interval_end,intervals[i][1])
            else:
                res.append([non_merge_interval_start,non_merge_interval_end])
                non_merge_interval_start =intervals[i][0]
                non_merge_interval_end =intervals[i][1]
        
        if ([non_merge_interval_start,non_merge_interval_end]) not in res:
            res.append([non_merge_interval_start,non_merge_interval_end])
        # else:            
        #     last_index = len(intervals)-1
        #     res.append([intervals[last_index][0],intervals[last_index][1]])

        return res



