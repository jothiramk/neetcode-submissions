class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        result = []
        intervals.sort()
        first = intervals[0]

        for i in range (1 , len(intervals)):            
            second = intervals[i]
            # print(f'first is {first} and second is {second}')
            #if there is an overlap we merge
            if second[0] <= first[1]:
                first = [min(first[0],second[0]),max(first[1],second[1])]
                # print(f'perfomred a merge {first}')
            else:
                result.append(first)
                first = second
                # print(f' no merge so appending result is {result} and first is {first}')
        result.append(first)
        return result

        