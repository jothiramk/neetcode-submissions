class Solution:
    def generateParenthesis(self, n: int) -> List[str]:

       
        res = []
        stack = []
        def dfs(openN, closeN):
            # print(f'{openN} {closeN} {n}')
            if openN == n and  closeN == n:
                res.append("".join(stack))
                return
            
            if openN < n :
                stack.append('(')
                # print(f'openN {stack}')
                dfs(openN+1, closeN)
                stack.pop()
            if closeN < openN:
                stack.append(')')
                dfs(openN,closeN+1)
                stack.pop()
            # print('jothi')
    
        dfs(0,0)
        return res
