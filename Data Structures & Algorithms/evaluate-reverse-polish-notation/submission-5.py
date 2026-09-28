class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []
        for token in tokens:
            if token in ('+','-','*','/'):
                # print(f'token in {token}')
                if len(stack)>1:
                    second_operand = stack.pop()
                    first_operand = stack.pop()
                    if token == '+':
                        res = first_operand + second_operand
                    elif token == '-':
                        res = first_operand - second_operand
                    elif token == '*':
                        res = first_operand * second_operand
                    elif token == '/':
                        res = int(first_operand / second_operand)
                    # print(f'first_operand is {first_operand} and second_operand is {second_operand} and res {res}')
                    stack.append(res)
            else:
                stack.append(int(token))
           
        return stack[0]