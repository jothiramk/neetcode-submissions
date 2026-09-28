class Solution:
    def isHappy(self, n: int) -> bool:
        seen = set()

        while n:
            if n == 1:
                return True
            temp = n
            n = 0
            while temp:
                rem = temp%10
                temp = temp//10
                n+=rem**2
            
            if n in seen:
                return False
            seen.add(n)
        
        return 
