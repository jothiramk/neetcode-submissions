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
            print(f'processing {ch} leftMin is {leftMin} and leftMax is {leftMax}')            
            if leftMax < 0:
                return False
            # we do this since we do not want to consider every * to be right parantesis
            if leftMin < 0:
                leftMin = 0
            
        return leftMin == 0


# About that part where we reset leftMin to 0 if it's negative. Take for example a string that looks like this  "(((***". After we have parsed this string our leftMax wil be 6 and our leftMin will be 0 which should return true because we can change every asterisk symbol for a right parenthesis symbol. But if we add another asterisk to that string "(((****" our leftMin will become -1. But in this case it doesn't make any sense for us to turn every asterisk into a right parenthesis because it will make the whole string invalid, that's why we treat one asterisk as an empty string and reset our leftMin to 0