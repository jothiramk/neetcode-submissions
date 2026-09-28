class Solution:
    def checkValidString(self, s: str) -> bool:
        leftMin, leftMax = 0, 0

        for i,ch in enumerate(s):
            if ch in '(':
                leftMin = leftMin+1 
                leftMax = leftMax+1
            elif ch in ')':
                leftMin = leftMin-1 
                leftMax = leftMax-1
            else:
                #when we consider * as right pare we subtract
                leftMin = leftMin-1  
                #when we consider * as left pare we subtract
                leftMax = leftMax+1
            
            if leftMax < 0:
                return False
            if leftMin < 0:
                leftMin = 0
            
        return leftMin == 0