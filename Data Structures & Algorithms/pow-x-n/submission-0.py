class Solution:
    def myPow(self, x: float, n: int) -> float:

        def helper(x:flaot, n:int):
            if x == 0:
                return 0
            if n == 0:
                return 1
            print(n)
            res = helper(x,n//2)
            res = res*res
            if n %2 != 0:
                res = res * x
            return res
            
        
        res = helper(x,abs(n))
        return res if n>0 else (1/res)
        