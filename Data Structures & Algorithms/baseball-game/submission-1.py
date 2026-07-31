class Solution:
    def calPoints(self, operations: List[str]) -> int:

        result = []
        for operation in operations:
            if operation == '+':
                result_size = len(result)
                result.append(result[result_size-1]+result[result_size-2])
            elif operation == 'C':
                result.pop()
            elif operation == 'D':
                result.append(result[-1] * 2)
            else:
                result.append(int(operation))
        score = 0

        return sum(result)


        