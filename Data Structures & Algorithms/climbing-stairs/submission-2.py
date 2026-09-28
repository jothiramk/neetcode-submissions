class Solution:

    def memoization(self, n:int , cache:dict) -> int:
        if n <= 2:
            return n
        elif n in cache:
            return cache[n]
        
        cache[n] =  self.memoization(n-1,cache) + self.memoization(n-2,cache)
        return cache[n]

    def climbStairs(self, n: int) -> int:
        cache = {}
        return self.memoization(n,cache)
        
