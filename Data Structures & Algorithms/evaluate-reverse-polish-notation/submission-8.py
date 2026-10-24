class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []
        for token in tokens:
            if token == '+':
                stack.append(stack.pop()+stack.pop())
            elif token == '-':
                first_elem = stack.pop()
                second_elem = stack.pop()
                stack.append(second_elem-first_elem)
                
            elif token == '*':
                stack.append(stack.pop()*stack.pop())
                
            elif token == '/':
                first_elem = stack.pop()
                second_elem = stack.pop()
                stack.append(int(second_elem/first_elem))
                
            else:
                stack.append(int(token))
            # print(f'stack is {stack}')
        
        return stack[0]
