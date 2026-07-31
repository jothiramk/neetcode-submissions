class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        for ch in s:
            if ch in '{[(':
                stack.append(ch)
            elif len(stack) == 0 and ch in ')}]':
                return False
            elif ch == ']' and stack[-1] != '[':
                return False
            elif ch == '}' and stack[-1] != '{':
                return False
            elif ch == ')' and stack[-1] != '(':
                return False
            else:
                stack.pop(-1)

        if stack != []:
            return False
        else:
            return True
                
            
