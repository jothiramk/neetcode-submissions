class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        #build a monotonic decreasing stack
        stack = []
        result = [0] * len(temperatures)
        for i , temp in enumerate(temperatures):
            while stack and temperatures[stack[-1]] < temp:
                j = stack.pop()
                # print(f'j index is {j}  ')
                result[j] = i - j
            
            stack.append(i)
            
        
        return result

        