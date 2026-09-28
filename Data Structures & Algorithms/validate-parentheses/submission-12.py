class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        for brace in range(len(s)):
            if s[brace] in (')','}',']') and not stack:
                return False
            elif s[brace] == ')' and stack[-1] == '(':
                stack.pop()
            elif s[brace] == ']' and stack[-1] == '[':
                stack.pop()
            elif s[brace] == '}' and stack[-1] == '{':
                stack.pop()           
            else:
                stack.append(s[brace])
        
        return True if not stack else False