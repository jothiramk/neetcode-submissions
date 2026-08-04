class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []
        operators = ['+','*','-','/']
        for token in tokens:
            if token in operators:
                # if len(stack) < 2:
                second_val = stack.pop()
                first_val = stack.pop()
                if token == '+':
                    res = first_val + second_val
                elif token == '-':
                    res = first_val - second_val
                elif token == '*':
                    res = first_val * second_val
                elif token == '/':
                    res = int(first_val / second_val)
                # print(f'first_val {first_val} and second_val {second_val} and token {token} and  res {res}')
                stack.append(res)
            else:
                stack.append(int(token))
        return stack[0]