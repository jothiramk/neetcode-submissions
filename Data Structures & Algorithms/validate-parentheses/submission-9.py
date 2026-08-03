class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        closed_parentheses = [')','}',']']
        open_parentheses = ['(','{','[']
        for ch in s:
            if ch in closed_parentheses and not stack:
                return False
            
            if ch in open_parentheses:
                stack.append(ch)

            elif ch in ')' and stack[-1] != '(':
                return False
            elif ch in ']' and stack[-1] != '[':
                return False
            elif ch in '}' and stack[-1] != '{':
                return False
            else:
                stack.pop()
        if stack:
            return False
        return True