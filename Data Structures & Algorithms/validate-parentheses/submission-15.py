class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        for ch in s:
            # print(f'processing {ch} and stack is {stack}')
            if ch in '{[(':
                stack.append(ch)
            elif not stack and ch in '}])':
                return False
            elif stack and ch == '}' and stack[-1] != '{':
                return False
            elif stack and ch == ']' and stack[-1] != '[':
                return False
            elif stack and ch == ')' and stack[-1] != '(':
                return False
            else:
                stack.pop()
            
        # print(len(stack))
        if len(stack) == 0:
            return True
        else:
            return False