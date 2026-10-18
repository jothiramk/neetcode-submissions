class Solution:
    def calPoints(self, operations: List[str]) -> int:
        stack = []
        for operation in operations:
            if operation == "+":
                stack.append(int(stack[-1]+stack[-2]))
            elif operation == "D":
                stack.append(int(stack[-1]*2))
            elif operation == "C":
                stack.pop()
                # print(f'after poppiong {stack}')
            else:
                stack.append(int(operation))
            # print(stack)
        return sum(stack)