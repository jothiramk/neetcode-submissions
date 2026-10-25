class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        intervals.sort()
        # print(intervals)
        result = []
        first = intervals[0]
        for i in range(1, len(intervals)):
            if intervals[i][0] <= first[1]:
                first = [first[0],max(first[1],intervals[i][1])]
                print(first)
            else:
                result.append(first)
                first = intervals[i]
        
        result.append(first)

        return result