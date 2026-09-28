class Solution:
    def hammingWeight(self, n: int) -> int:
        res = 0
        #23 --> 10111 
        while n > 0:
            if n & 1:
                res += 1
            n = n >> 1
        
        return res