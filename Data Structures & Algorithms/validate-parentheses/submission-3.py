class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        open_brace = ['(','{','[']
        for ch in s:
            if ch in open_brace:
                stack.append(ch)
            elif len(stack) == 0:
                return False
            elif ch == ')' :
                if stack[-1] == '(':
                    stack.pop()
                else:
                    return False
            elif ch =='}':
                if stack[-1] == '{':
                    stack.pop()
                else:
                    return False
            elif ch ==']':
                if stack[-1] == '[':
                    stack.pop()
                else:
                    return False
        
        if len(stack) == 0:
            return True
        
        return False

